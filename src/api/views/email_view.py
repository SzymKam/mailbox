from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from api.serializers.email_serializer import EmailSerializer
from management.models import Email


class EmailView(GenericViewSet, CreateModelMixin, ListModelMixin):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
