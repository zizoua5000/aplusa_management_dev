from rest_framework.serializers import ModelSerializer,SerializerMethodField
from simcard.api.models import Simcard
# from device.api.serializers import DeviceSerializer

class SimcardSerializer(ModelSerializer):
        # device_detail=SerializerMethodField()
        class Meta:
            model=Simcard
            fields=['id','number','package','has_rouming','is_active','created_at','updated_at']


        # def get_device_detail(self,obj):
        #     return DeviceSerializer(obj.device).data

