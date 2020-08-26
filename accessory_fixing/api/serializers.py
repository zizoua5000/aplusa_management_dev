from rest_framework.serializers import ModelSerializer,SerializerMethodField
from accessory_fixing.api.models import AccessoryFixing
from accessory.api.serializers import AccessorySerializer
from company.api.serializers import CompanySerializer
from vehicle.api.serializers import VehicleSerializer
from status.api.serializers import StatusSerializer

class AccessoryFixingSerializer(ModelSerializer):
        accessory_detail=SerializerMethodField()
        company_detail=SerializerMethodField()
        vehicle_detail=SerializerMethodField()
        accessory_status_detail=SerializerMethodField()
        class Meta:
            model=AccessoryFixing
            fields=[
                'id',
                'accessory',
                'accessory_detail',
                'company',
                'company_detail',
                'vehicle',
                'vehicle_detail',
                'accessory_status',
                'accessory_status_detail',
                'accessory_event_datetime',
                'comment',
                'created_at',
                'updated_at'
                ]
        def get_accessory_detail(self,obj):
            return AccessorySerializer(obj.accessory).data
        def get_company_detail(self,obj):
            return CompanySerializer(obj.company).data
        def get_vehicle_detail(self,obj):
            return VehicleSerializer(obj.vehicle).data
        def get_accessory_status_detail(self,obj):
            return StatusSerializer(obj.accessory_status).data

