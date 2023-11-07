from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone

from .mailbox_model import Mailbox
from .template_model import Template


class Email(models.Model):
    mailbox = models.ForeignKey(Mailbox, on_delete=models.CASCADE, related_name="email")
    template = models.ForeignKey(Template, on_delete=models.DO_NOTHING, related_name="email")
    to = ArrayField(base_field=models.EmailField())
    cc = ArrayField(base_field=models.EmailField(), blank=True, null=True)
    bcc = ArrayField(base_field=models.EmailField(), blank=True, null=True)
    reply_to = models.EmailField(default=None, blank=True, null=True)
    send_date = models.DateTimeField(blank=True, null=True, default=None)
    date = models.DateTimeField(default=timezone.now)
