from rest_framework.serializers import ModelSerializer,SerializerMethodField
from device_model.api.models import DeviceModel
from device_mark.api.serializers import DeviceMarkSerializer

class DeviceModelSerializer(ModelSerializer):
        device_mark_detail=SerializerMethodField()
        class Meta:
            model=DeviceModel
            fields=['id','name','device_mark','device_mark_detail','created_at','updated_at']

        def get_device_mark_detail(self,obj):
            return DeviceMarkSerializer(obj.device_mark).data

