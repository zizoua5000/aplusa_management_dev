from rest_framework.serializers import ModelSerializer
from device_location.api.models import DeviceLocation

class DeviceLocationSerializer(ModelSerializer):
        class Meta:
            model=DeviceLocation
            fields=['id','name','created_at','updated_at']



