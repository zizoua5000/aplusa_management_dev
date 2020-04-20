from rest_framework.serializers import ModelSerializer,SerializerMethodField
from price.api.models import Price
from price_type.api.serializers import PriceTypeSerializer
from device_model.api.serializers import DeviceModelSerializer
from accessory_model.api.serializers import AccessoryModelSerializer
from project.api.serializers import ProjectSerializer

class PriceSerializer(ModelSerializer):
        price_type_detail=SerializerMethodField()
        device_model_detail=SerializerMethodField()
        accessory_model_detail=SerializerMethodField()
        project_detail=SerializerMethodField()
        
        class Meta:
            model=Price
            fields=[
                'id',
                'start_datetime',
                'end_datetime',
                'price_type',
                'price_type_detail',
                'sell_price',
                'project',
                'project_detail',
                'device_model',
                'device_model_detail',
                'accessory_model',
                'accessory_model_detail',
                'is_second_hand'
                ]

        def get_price_type_detail(self,obj):
            return PriceTypeSerializer(obj.price_type).data
        def get_device_model_detail(self,obj):\
            return DeviceModelSerializer(obj.device_model).data
        def get_accessory_model_detail(self,obj):
            return AccessoryModelSerializer(obj.accessory_model).data
        def get_project_detail(self,obj):
            return ProjectSerializer(obj.project).data
        

