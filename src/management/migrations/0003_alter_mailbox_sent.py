# Generated by Django 4.2.7 on 2023-11-14 22:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("management", "0002_email_bcc_alter_email_cc"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailbox",
            name="sent",
            field=models.IntegerField(blank=True, default=0),
        ),
    ]