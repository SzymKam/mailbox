from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from api.serializers.mailbox_serializer import MailboxSerializer
from management.models import Mailbox


class MailboxView(ModelViewSet):
    queryset = Mailbox.objects.all()
    serializer_class = MailboxSerializer
