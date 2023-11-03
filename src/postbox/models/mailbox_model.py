from django.utils import timezone
from django.db import models


class Mailbox(models.Model):
    host = models.CharField()
    port = models.IntegerField(default=465)
    login = models.CharField()
    password = models.CharField()
    email_from = models.EmailField()
    use_ssl = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now(), null=True, blank=True)
    last_update = models.DateTimeField(default=timezone.now(), null=True, blank=True)
    sent = models.IntegerField(null=True, blank=True)



