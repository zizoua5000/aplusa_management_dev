from rest_framework.serializers import ModelSerializer,SerializerMethodField
from device_detail.api.models import DeviceDetail
from status.api.serializers import StatusSerializer
from simcard.api.serializers import SimcardSerializer
from vehicle.api.serializers import VehicleSerializer
from company.api.serializers import CompanySerializer
from person.api.serializers import PersonSerializer
from device_location.api.serializers import DeviceLocationSerializer
from configuration.api.serializers import ConfigurationSerializer
from project.api.serializers import ProjectSerializer
from region.api.serializers import RegionSerializer
from fw_version.api.serializers import FWVersionSerializer

class DeviceDetailSerializer(ModelSerializer):
        status_detail=SerializerMethodField()
        simcard_detail=SerializerMethodField()
        vehicle_detail=SerializerMethodField()
        company_detail=SerializerMethodField()
        recipient_detail=SerializerMethodField()
        device_location_detail=SerializerMethodField()
        configuration_detail=SerializerMethodField()
        project_detail=SerializerMethodField()
        region_detail=SerializerMethodField()
        fw_version_detail=SerializerMethodField()

        class Meta:
            model=DeviceDetail
            fields=[
                'id',
                'status',
                'status_detail',
                'simcard',
                'simcard_detail',
                'vehicle',
                'vehicle_detail',
                'company',
                'company_detail',
                'recipient',
                'recipient_detail',
                'device_location',
                'device_location_detail',
                'configuration',
                'configuration_detail',
                'fw_version',
                'fw_version_detail',
                'project',
                'project_detail',
                'region',
                'region_detail',
                'comment',
                'price_datetime',
                'status_datetime',
                'sell_count'
                ]

        def get_status_detail(self,obj):
            return StatusSerializer(obj.status).data
        def get_simcard_detail(self,obj):
            return SimcardSerializer(obj.simcard).data
        def get_vehicle_detail(self,obj):
            return VehicleSerializer(obj.vehicle).data
        def get_company_detail(self,obj):
            return CompanySerializer(obj.company).data
        def get_recipient_detail(self,obj):
            return PersonSerializer(obj.recipient).data
        def get_device_location_detail(self,obj):
            return DeviceLocationSerializer(obj.device_location).data
        def get_configuration_detail(self,obj):
            return ConfigurationSerializer(obj.configuration).data
        def get_project_detail(self,obj):
            return ProjectSerializer(obj.project).data
        def get_region_detail(self,obj):
            return RegionSerializer(obj.region).data
        def get_fw_version_detail(self,obj):
            return FWVersionSerializer(obj.fw_version).data

       