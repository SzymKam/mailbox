from celery import shared_task
from django.core.mail import EmailMessage


@shared_task
def _email_sending(self):
    email = EmailMessage(
        subject=self.template.subject,
        body=self.template.text,
        from_email=self.mailbox.email_from,
        to=self.to,
        cc=self.cc,
        bcc=self.bcc,
        reply_to=self.reply_to,
        attachments=self.template.attachment,
    )
    email.send()
