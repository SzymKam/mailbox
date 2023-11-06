from rest_framework.serializers import ModelSerializer, ValidationError

from management.models import Template


class TemplateSerializer(ModelSerializer):
    class Meta:
        model = Template
        fields = "__all__"

    def validate(self, data):
        subject = data.get("subject")
        if Template.objects.filter(subject=subject).exists():
            raise ValidationError("This template is already in use.")
        return data
