from django.db import models
from django.utils import timezone


class Template(models.Model):
    subject = models.CharField()
    text = models.TextField()
    attachment = models.FileField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now(), null=True, blank=True)
    last_update = models.DateTimeField(default=timezone.now(), null=True, blank=True)


