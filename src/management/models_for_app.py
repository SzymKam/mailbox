# from django.contrib.postgres.fields import ArrayField
# from django.db import models
# from django.utils import timezone
#
#
# class Mailbox(models.Model):
#     host = models.CharField()
#     port = models.IntegerField(default=465)
#     login = models.CharField(max_length=50)
#     password = models.CharField()
#     email_from = models.EmailField()
#     use_ssl = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=False, null=True, blank=True)
#     date = models.DateTimeField(default=timezone.now, null=True, blank=True)
#     last_update = models.DateTimeField(default=timezone.now, null=True, blank=True)
#     sent = models.IntegerField(null=True, blank=True)
#
#
# class Template(models.Model):
#     subject = models.CharField()
#     text = models.TextField()
#     attachment = models.FileField(blank=True, null=True)
#     date = models.DateTimeField(default=timezone.now, null=True, blank=True)
#     last_update = models.DateTimeField(default=timezone.now, null=True, blank=True)


# class Email(models.Model):
#     mailbox = models.ForeignKey(Mailbox, on_delete=models.CASCADE, related_name="email")
# template = models.ForeignKey(Template, on_delete=models.DO_NOTHING, related_name="email")
# to = ArrayField(base_field=models.EmailField())
# cc = ArrayField(base_field=models.EmailField())
# reply_to = models.EmailField(default=None, blank=True, null=True)
# send_date = models.DateTimeField(blank=True, null=True, default=None)
# date = models.DateTimeField(default=timezone.now)
