from rest_framework.serializers import ModelSerializer
from status.api.models import Status

class StatusSerializer(ModelSerializer):
        class Meta:
            model=Status
            fields=['id','name','created_at','updated_at']



