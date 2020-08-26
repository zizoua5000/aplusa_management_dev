from rest_framework.serializers import ModelSerializer,SerializerMethodField
from accessory_history.api.models import AccessoryHistory
from accessory.api.serializers import AccessorySerializer
from company.api.serializers import CompanySerializer

class AccessoryHistorySerializer(ModelSerializer):
        accessory_detail=SerializerMethodField()
        manufacturer_detail=SerializerMethodField()
        class Meta:
            model=AccessoryHistory
            fields=[
                'id',
                'accessory',
                'accessory_detail',
                'manufacturer',
                'manufacturer_detail',
                'rated_price',
                'count',
                'created_at',
                'updated_at'
                ]
        def get_accessory_detail(self,obj):
            return AccessorySerializer(obj.accessory).data
        def get_manufacturer_detail(self,obj):
            return CompanySerializer(obj.manufacturer).data

