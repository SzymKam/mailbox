from django.utils import timezone
from rest_framework.viewsets import ModelViewSet

from api.serializers.template_serializer import TemplateSerializer
from management.models import Template


class TemplateView(ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

    def perform_create(self, serializer):
        serializer.validated_data["date"] = timezone.now()
        serializer.validated_data["last_update"] = timezone.now()
        serializer.save()

    def perform_update(self, serializer):
        serializer.validated_data["last_update"] = timezone.now()
        serializer.save()
