from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from .models import Mailbox, Template


class EmailManagement:
    def __init__(self, data: dict):
        self.data = data
        self._unpack_data()

    def _unpack_data(self):
        self.to = self.data.get("to")
        self.cc = self.data.get("cc")
        self.bcc = self.data.get("bcc")
        self.reply_to = self.data.get("reply_to")
        self.send_date = self.data.get("send_date")
        self.mailbox = get_object_or_404(klass=Mailbox, id=self.data.get("mailbox"))
        self.template = get_object_or_404(klass=Template, id=self.data.get("template"))

    def email_sending(self):
        send_mail(
            subject="Szymon",
            from_email="szymon15kaminski@gmail.com",
            message="koza",
            recipient_list=["szymon15kaminski@gmail.com"],
        )
