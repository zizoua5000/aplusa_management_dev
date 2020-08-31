from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from pending.api.models import Pending
from project.api.serializers import ProjectSerializer
from company.api.serializers import CompanySerializer
from device.api.serializers import DeviceSerializer
from person.api.serializers import PersonSerializer
from status.api.serializers import StatusSerializer
from accessory.api.serializers import AccessorySerializer

class PendingSerializer(ModelSerializer):
        project_detail=SerializerMethodField()
        company_detail=SerializerMethodField()
        accessory_detail=SerializerMethodField()
        device_detail=SerializerMethodField()
        recipient_detail=SerializerMethodField()

        class Meta:
            model=Pending
            fields=['id','accessory','accessory_detail','company','company_detail','device','device_detail',
            'recipient','recipient_detail','project','project_detail','count','created_at','updated_at']

        def get_project_detail(self,obj):
            return ProjectSerializer(obj.project).data
        def get_company_detail(self,obj):
            return CompanySerializer(obj.company).data
        def get_accessory_detail(self,obj):
            return AccessorySerializer(obj.accessory).data
        def get_recipient_detail(self,obj):
            return PersonSerializer(obj.recipient).data
        def get_device_detail(self,obj):
            return DeviceSerializer(obj.device).data
                    
            
