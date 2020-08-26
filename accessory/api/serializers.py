from rest_framework.serializers import ModelSerializer,SerializerMethodField
from accessory.api.models import Accessory
from accessory_model.api.serializers import AccessoryModelSerializer
from accessory_type.api.serializers import AccessoryTypeSerializer

class AccessorySerializer(ModelSerializer):
        accessory_model_detail=SerializerMethodField()
        accessory_type_detail=SerializerMethodField()
        class Meta:
            model=Accessory
            fields=[
                'id',
                'name',
                'accessory_model',
                'accessory_model_detail',
                'accessory_type',
                'accessory_type_detail',
                'is_new',
                'is_our',
                'count',
                'created_at',
                'updated_at'
                ]
        def get_accessory_model_detail(self,obj):
            return AccessoryModelSerializer(obj.accessory_model).data
        def get_accessory_type_detail(self,obj):
            return AccessoryTypeSerializer(obj.accessory_type).data

