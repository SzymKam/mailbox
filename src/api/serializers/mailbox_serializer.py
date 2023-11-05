from rest_framework.serializers import ModelSerializer

from management.models import Mailbox


class MailboxSerializer(ModelSerializer):
    class Meta:
        model = Mailbox
        fields = "__all__"
