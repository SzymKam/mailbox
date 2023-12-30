from celery import shared_task
from django.core.mail import EmailMessage


@shared_task(bind=True)
def email_sending(self, template: dict, mailbox: dict, to: str, cc: str, bcc: str, reply_to: str) -> str:
    email = EmailMessage(
        subject=template.get("subject"),
        body=template.get("text"),
        from_email=mailbox.get("email_from"),
        to=to,
        cc=cc,
        bcc=bcc,
        reply_to=reply_to,
        attachments=template.get("attachments"),
    )
    email.send()
    return f"Email sent to {to}"
