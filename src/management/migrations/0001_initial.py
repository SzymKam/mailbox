# Generated by Django 4.2.7 on 2023-11-04 20:46

import django.contrib.postgres.fields
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Mailbox",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("host", models.CharField()),
                ("port", models.IntegerField(default=465)),
                ("login", models.CharField(max_length=50)),
                ("password", models.CharField()),
                ("email_from", models.EmailField(max_length=254)),
                ("use_ssl", models.BooleanField(default=True)),
                ("is_active", models.BooleanField(blank=True, default=False, null=True)),
                ("date", models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ("last_update", models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ("sent", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Template",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("subject", models.CharField()),
                ("text", models.TextField()),
                ("attachment", models.FileField(blank=True, null=True, upload_to="")),
                ("date", models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ("last_update", models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Email",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "to",
                    django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254), size=None),
                ),
                (
                    "cc",
                    django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254), size=None),
                ),
                ("reply_to", models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ("send_date", models.DateTimeField(blank=True, default=None, null=True)),
                ("date", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "mailbox",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="email", to="management.mailbox"
                    ),
                ),
                (
                    "template",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, related_name="email", to="management.template"
                    ),
                ),
            ],
        ),
    ]