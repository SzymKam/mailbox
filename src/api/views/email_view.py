from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from api.serializers.email_serializer import EmailSerializer
from management.models import Email
from management.views.email_management_view import EmailManagement


class EmailView(GenericViewSet, CreateModelMixin, ListModelMixin):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        email_management = EmailManagement(data=serializer.data, headers=headers)
        email_management.sending_attempt()
