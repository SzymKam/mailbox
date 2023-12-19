from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from .models import Mailbox, Template
from .tasks import email_sending


class EmailManagement:
    def __init__(self, data: dict, headers: dict) -> None:
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

    def send(self):
        if self.mailbox.is_active:
            email_sending.delay(
                template=self.template,
                mailbox=self.mailbox,
                to=self.to,
            )
            self.mailbox.sent += 1
            self.mailbox.save()
            return Response("Email send", status=status.HTTP_201_CREATED, headers=self.headers)

        else:
            return Response("Mailbox is not active", status=status.HTTP_400_BAD_REQUEST, headers=self.headers)
