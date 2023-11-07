from django.core.mail import send_mail
from django.shortcuts import render


def email_sending():
    send_mail(
        subject="Szymon",
        from_email="szymon15kaminski@gmail.com",
        message="koza",
        recipient_list=["szymon15kaminski@gmail.com"],
    )
