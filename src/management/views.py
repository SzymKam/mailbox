from django.core.mail import EmailMessage, send_mail
from django.shortcuts import get_object_or_404

from .models import Mailbox, Template


class EmailManagement:
    def __init__(self, data: dict):
        self.data = data
        self._unpack_data()
        self._email_sending()

    def _unpack_data(self):
        self.to = self.data.get("to")
        self.cc = self.data.get("cc")
        self.bcc = self.data.get("bcc")
        self.reply_to = self.data.get("reply_to")
        self.send_date = self.data.get("send_date")
        self.mailbox = get_object_or_404(klass=Mailbox, id=self.data.get("mailbox"))
        self.template = get_object_or_404(klass=Template, id=self.data.get("template"))

    def _email_sending(self):
        send_mail(
            subject=self.template.subject,
            from_email="szymon15kaminski@gmail.com",
            message=self.template.text,
            recipient_list=["szymon15kaminski@gmail.com"],
        )


def xyz():
    ...
    # 1) Sprawdza czy dane do wykresu znajdują się w redis np. {'submissions': {'2023-01-01': 3}}
    # 2) Renderuje jakis wykres

    # 1) Sprawdza ale dane się nie znajdują
    # 2) Robi zapytanie do bazy danych lub zewnętrznego API.
    # 3) Renderuje jakiś wykres
    # 4) Cachuje dane np. na 5 minut.

    #
