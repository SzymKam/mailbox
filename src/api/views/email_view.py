from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from api.serializers.email_serializer import EmailSerializer
from management.models import Email
from management.views import EmailManagement


class EmailView(GenericViewSet, CreateModelMixin, ListModelMixin):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

    def perform_create(self, serializer):
        email_management = EmailManagement(data=serializer.data)
