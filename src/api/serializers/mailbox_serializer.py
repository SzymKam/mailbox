from rest_framework.serializers import ModelSerializer, ValidationError

from management.models import Mailbox


class MailboxSerializer(ModelSerializer):
    class Meta:
        model = Mailbox
        fields = "__all__"

    def validate(self, data):
        email = data.get("email_from")
        if Mailbox.objects.filter(email_from=email).exists():
            raise ValidationError("Email is already in use.")

        login = data.get("login")
        if Mailbox.objects.filter(login=login).exists():
            raise ValidationError("Login is already in use.")

        return data
