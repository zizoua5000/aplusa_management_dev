from rest_framework.serializers import ModelSerializer,SerializerMethodField
from accessory.api.models import Accessory
from company.api.serializers import CompanySerializer
from accessory_model.api.serializers import AccessoryModelSerializer
from accessory_type.api.serializers import AccessoryTypeSerializer

class AccessorySerializer(ModelSerializer):
        company_detail=SerializerMethodField()
        accessory_model_detail=SerializerMethodField()
        accessory_type_detail=SerializerMethodField()
        class Meta:
            model=Accessory
            fields=[
                'id',
                'name',
                'company',
                'company_detail',
                'accessory_model',
                'accessory_model_detail',
                'accessory_type',
                'accessory_type_detail',
                'created_at',
                'updated_at'
                ]
        def get_company_detail(self,obj):
            return CompanySerializer(obj.company).data
        def get_accessory_model_detail(self,obj):
            return AccessoryModelSerializer(obj.accessory_model).data
        def get_accessory_type_detail(self,obj):
            return AccessoryTypeSerializer(obj.accessory_type).data

