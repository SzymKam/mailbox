from django.core.exceptions import BadRequest
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from .models import Mailbox, Template
from .tasks import email_sending


class EmailManagement:
    def __init__(self, data: dict) -> None:
        self.data = data
        self._unpack_data()
        self._get_mailbox_settings()

    def _unpack_data(self):
        self.to = self.data.get("to")
        self.cc = self.data.get("cc")
        self.bcc = self.data.get("bcc")
        self.reply_to = self.data.get("reply_to")
        self.send_date = self.data.get("send_date")
        self.mailbox = get_object_or_404(klass=Mailbox, id=self.data.get("mailbox"))
        self.template = get_object_or_404(klass=Template, id=self.data.get("template"))

    def _get_mailbox_settings(self):
        self.host = self.mailbox.host
        self.port = self.mailbox.port
        self.use_ssl = self.mailbox.use_ssl

        # self._email_sending()

    # def run(self):
    #     email_sending.delay()

    # def _send_email(self):

    #         self.mailbox.sent += 1
    #         self.mailbox.save()
    #
    #     else:
    #         return Response("Mailbox is not active", status=status.HTTP_400_BAD_REQUEST)
