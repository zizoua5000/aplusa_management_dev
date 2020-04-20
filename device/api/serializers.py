from rest_framework.serializers import ModelSerializer,SerializerMethodField
from device.api.models import Device
from company.api.serializers import CompanySerializer
from device_model.api.serializers import DeviceModelSerializer
from device_type.api.serializers import DeviceTypeSerializer
from device_detail.api.serializers import DeviceDetailSerializer

class DeviceSerializer(ModelSerializer):
        company_detail=SerializerMethodField()
        device_model_detail=SerializerMethodField()
        device_type_detail=SerializerMethodField()
        device_detail_detail=SerializerMethodField()
        class Meta:
            model=Device
            fields=[
                'id',
                'serie',
                'company',
                'company_detail',
                'device_model',
                'device_model_detail',
                'device_type',
                'device_type_detail',
                'device_detail',
                'device_detail_detail',
                'created_at',
                'updated_at'
                ]

        def get_company_detail(self,obj):
            return CompanySerializer(obj.company).data
        def get_device_model_detail(self,obj):
            return DeviceModelSerializer(obj.device_model).data
        def get_device_type_detail(self,obj):
            return DeviceTypeSerializer(obj.device_type).data
        def get_device_detail_detail(self,obj):
            return DeviceDetailSerializer(obj.device_detail).data

