from rest_framework.serializers import ModelSerializer,SerializerMethodField
from accessory_history.api.models import AccessoryHistory
from accessory_model.api.serializers import AccessoryModelSerializer
from accessory_type.api.serializers import AccessoryTypeSerializer
from accessory.api.serializers import AccessorySerializer
from company.api.serializers import CompanySerializer

class AccessoryHistorySerializer(ModelSerializer):
        accessory_detail=SerializerMethodField()
        accessory_model_detail=SerializerMethodField()
        accessory_type_detail=SerializerMethodField()
        manufacturer_detail = SerializerMethodField()
        class Meta:
            model=AccessoryHistory
            fields=[
                'id',
                'name',
                'accessory',
                'accessory_detail',
                'accessory_model',
                'accessory_model_detail',
                'accessory_type',
                'accessory_type_detail',
                'manufacturer',
                'manufacturer_detail',
                'is_new',
                'is_our',
                'count',
                'rated_price',
                'entry_warehouse_date',
                'created_at',
                ]
        def get_accessory_detail(self,obj):
            return AccessorySerializer(obj.accessory).data
        def get_accessory_model_detail(self,obj):
            return AccessoryModelSerializer(obj.accessory_model).data
        def get_accessory_type_detail(self,obj):
            return AccessoryTypeSerializer(obj.accessory_type).data
        def get_manufacturer_detail(self,obj):
            return CompanySerializer(obj.manufacturer).data           

