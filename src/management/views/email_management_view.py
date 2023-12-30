from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from api.serializers.mailbox_serializer import MailboxSerializer
from api.serializers.template_serializer import TemplateSerializer

from ..models import Mailbox, Template
from ..tasks import email_sending
from .error_report_view import ReportBug


class EmailManagement:
    def __init__(self, data: dict, headers: dict) -> None:
        self.attempt = 1
        self.data = data
        self.headers = headers
        self._unpack_data()
        self._get_mailbox_settings()

    def _unpack_data(self) -> None:
        self.to = self.data.get("to")
        self.cc = self.data.get("cc")
        self.bcc = self.data.get("bcc")
        self.reply_to = self.data.get("reply_to")
        self.send_date = self.data.get("send_date")
        self.mailbox = get_object_or_404(klass=Mailbox, id=self.data.get("mailbox"))
        self.template = get_object_or_404(klass=Template, id=self.data.get("template"))

    def _get_mailbox_settings(self) -> None:
        self.host = self.mailbox.host
        self.port = self.mailbox.port
        self.use_ssl = self.mailbox.use_ssl

    def _template_serializer(self):
        template_data = TemplateSerializer(instance=self.template).data
        return template_data

    def _mailbox_serializer(self):
        mailbox_data = MailboxSerializer(instance=self.mailbox).data
        return mailbox_data

    def sending_attempt(self) -> Response:
        success = False

        if self.mailbox.is_active:
            for _ in range(3):
                if self._send():
                    success = True
                    break

            if success:
                return Response("Mail send", status=status.HTTP_201_CREATED, headers=self.headers)

            else:
                return Response(
                    data="Reached max attempt value. Check connection", status=status.HTTP_429_TOO_MANY_REQUESTS
                )
        else:
            return Response("Mailbox is not active", status=status.HTTP_400_BAD_REQUEST, headers=self.headers)

    def _send(self) -> bool:
        try:
            email_sending.delay(
                template=self._template_serializer(),
                mailbox=self._mailbox_serializer(),
                to=self.to,
                cc=self.cc,
                bcc=self.bcc,
                reply_to=self.reply_to,
            )
            self.mailbox.sent += 1
            self.mailbox.save()
            ReportBug(mailbox=self.mailbox, attempt=self.attempt).save_log_attempt_success()
            return True

        except Exception as error:
            ReportBug(mailbox=self.mailbox, attempt=self.attempt).save_log_attempt_failed(error=error)
            self.attempt += 1
            return False
