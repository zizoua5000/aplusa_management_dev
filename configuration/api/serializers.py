from rest_framework.serializers import ModelSerializer
from configuration.api.models import Configuration

class ConfigurationSerializer(ModelSerializer):
        class Meta:
            model=Configuration
            fields=['id','name','created_at','updated_at']



