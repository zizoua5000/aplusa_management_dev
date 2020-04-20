from rest_framework.serializers import ModelSerializer
from device_type.api.models import DeviceType

class DeviceTypeSerializer(ModelSerializer):
        class Meta:
            model=DeviceType
            fields=['id','name','created_at','updated_at']



