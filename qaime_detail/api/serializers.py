from rest_framework.serializers import ModelSerializer,SerializerMethodField
# from qaime.api.serializers import QaimeListSerializer
from device.api.serializers import DeviceSerializer
from accessory.api.serializers import AccessorySerializer
from simcard.api.serializers import SimcardSerializer
from project.api.serializers import ProjectSerializer
from company.api.serializers import CompanySerializer
from configuration.api.serializers import ConfigurationSerializer
from fw_version.api.serializers import FWVersionSerializer
from qaime_detail.api.models import QaimeDetail

class QaimeDetailListSerializer(ModelSerializer): 
        # qaime_detail=SerializerMethodField()
        device_detail=SerializerMethodField()
        accessory_detail=SerializerMethodField()
        simcard_detail=SerializerMethodField()
        project_detail=SerializerMethodField()
        company_detail=SerializerMethodField()
        configuration_detail=SerializerMethodField()
        fw_version_detail=SerializerMethodField()
        class Meta:
            model=QaimeDetail
            fields=[
                'id',
                'qaime',
                # 'qaime_detail',
                'device',
                'device_detail',
                'accessory',
                'accessory_detail',
                'simcard',
                'simcard_detail',
                'project',
                'project_detail',
                'company',
                'company_detail',
                'configuration',
                'configuration_detail',
                'fw_version',
                'fw_version_detail',
                'count',
                'is_new',
                'sold_or_rent',
                'created_at',
                'updated_at'
                ]
        # def get_qaime_detail(self,obj):
        #     return QaimeListSerializer(obj.qaime).data
        def get_device_detail(self,obj):
            return DeviceSerializer(obj.device).data
        def get_accessory_detail(self,obj):
            return AccessorySerializer(obj.accessory).data
        def get_simcard_detail(self,obj):
            return SimcardSerializer(obj.simcard).data
        def get_project_detail(self,obj):
            return ProjectSerializer(obj.project).data
        def get_company_detail(self,obj):
            return CompanySerializer(obj.company).data
        def get_configuration_detail(self,obj):
            return ConfigurationSerializer(obj.configuration).data
        def get_fw_version_detail(self,obj):
            return FWVersionSerializer(obj.fw_version).data 


