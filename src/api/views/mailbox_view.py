from django.utils import timezone
from rest_framework.viewsets import ModelViewSet

from api.serializers.mailbox_serializer import MailboxSerializer
from management.models import Mailbox


class MailboxView(ModelViewSet):
    queryset = Mailbox.objects.all()
    serializer_class = MailboxSerializer

    def perform_create(self, serializer) -> None:
        serializer.validated_data["date"] = timezone.now()
        serializer.validated_data["last_update"] = timezone.now()
        serializer.save()

    def perform_update(self, serializer) -> None:
        serializer.validated_data["last_update"] = timezone.now()
        serializer.save()
