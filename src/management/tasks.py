from celery import shared_task
from django.core.mail import EmailMessage

from .models import Mailbox, Template


@shared_task
def email_sending(template: Template, mailbox: Mailbox, to: str, cc: str, bcc: str, reply_to: str) -> None:
    email = EmailMessage(
        subject=template.subject,
        body=template.text,
        from_email=mailbox.email_from,
        to=to,
        cc=cc,
        bcc=bcc,
        reply_to=reply_to,
        attachments=template.attachment,
    )
    email.send()
