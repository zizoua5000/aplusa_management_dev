from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import ContentType

class ContentTypeSerializer(ModelSerializer):
        class Meta:
            model=ContentType
            fields=['id','app_label','model']



