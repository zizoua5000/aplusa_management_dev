from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from pending.api.models import Pending
from device.api.serializers import DeviceSerializer
from accessory.api.serializers import AccessorySerializer
from person.api.serializers import PersonSerializer
from project.api.serializers import ProjectSerializer
from company.api.serializers import CompanySerializer
from status.api.serializers import StatusSerializer

class PendingSerializer(ModelSerializer):
        device_detail=SerializerMethodField()
        accessory_detail=SerializerMethodField()
        recipient_detail=SerializerMethodField()
        project_detail=SerializerMethodField()
        company_detail=SerializerMethodField()
        status_detail=SerializerMethodField()
        class Meta:
            model=Pending
            fields=['id',
            'device','device_detail',
            'accessory','accessory_detail',
            'recipient','recipient_detail',
            'project','project_detail',
            'company','company_detail',
            'status','status_detail',
            'count','created_at'
            ]

        def get_device_detail(self,obj):
            return DeviceSerializer(obj.device).data
        def get_accessory_detail(self,obj):
            return AccessorySerializer(obj.accessory).data
        def get_recipient_detail(self,obj):
            return PersonSerializer(obj.recipient).data
        def get_project_detail(self,obj):
            return ProjectSerializer(obj.project).data
        def get_company_detail(self,obj):
            return CompanySerializer(obj.company).data
        def get_status_detail(self,obj):
            return StatusSerializer(obj.status).data
