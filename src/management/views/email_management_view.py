from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

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

    def sending_attempt(self) -> Response:
        if self.mailbox.is_active:
            # while self.attempt < 3:
            self._send()

            return Response(
                data="Reached max attempt value. Check connection", status=status.HTTP_429_TOO_MANY_REQUESTS
            )

        return Response("Mailbox is not active", status=status.HTTP_400_BAD_REQUEST, headers=self.headers)

    def _send(self) -> Response:
        print("sending")
        ReportBug(mailbox=self.mailbox, attempt=self.attempt).save_log_attempt_success()
        print("sending2")
        ReportBug(mailbox=self.mailbox, attempt=self.attempt).save_log_attempt_failed()

        # try:
        #     email_sending.delay(
        #         template=self.template,
        #         mailbox=self.mailbox,
        #         to=self.to,
        #     )
        #
        #
        # except Exception:
        #     pass
        #
        #

        # self.attempt += 1

        # try:
        #
        #
        #
        #     self.mailbox.sent += 1
        #     self.mailbox.save()
        #     return Response("Email send", status=status.HTTP_201_CREATED, headers=self.headers)
        #
        # except  as error:
        #
        #     ReportBug(mailbox=self.mailbox, attempt=self.attempt)
        #     self.attempt += 1
