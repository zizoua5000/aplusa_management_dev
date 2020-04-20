from rest_framework.serializers import ModelSerializer
from device_mark.api.models import DeviceMark

class DeviceMarkSerializer(ModelSerializer):
        class Meta:
            model=DeviceMark
            fields=['id','name','created_at','updated_at']



