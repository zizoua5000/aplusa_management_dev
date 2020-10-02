from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from accessory.api.models import Accessory
from accessory_history.api.models import AccessoryHistory
from accessory_model.api.serializers import AccessoryModelSerializer
from accessory_type.api.serializers import AccessoryTypeSerializer
from company.api.serializers import CompanySerializer

class AccessorySerializer(ModelSerializer):
        accessory_model_detail=SerializerMethodField()
        accessory_type_detail=SerializerMethodField()
        manufacturer_detail = SerializerMethodField()
        entry_warehouse_date = serializers.DateTimeField(format=None,input_formats=None)
        class Meta:
            model=Accessory
            fields=[
                'id',
                'name',
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
                'updated_at'
                ]
        def get_accessory_model_detail(self,obj):
            return AccessoryModelSerializer(obj.accessory_model).data
        def get_accessory_type_detail(self,obj):
            return AccessoryTypeSerializer(obj.accessory_type).data
        def get_manufacturer_detail(self,obj):
            return CompanySerializer(obj.manufacturer).data   

        def create(self, validated_data):
            print("INITIAL VALIDATED DATA: ",validated_data)
            accessory = Accessory.objects.create(**validated_data)
            print("ACCESSORY : ",validated_data)
            validated_data.update({'accessory_id':accessory.id})
            accessory_history = AccessoryHistory.objects.create(**validated_data)         
            return accessory     

        def update(self, instance, validated_data):
            print("INSTANCE",instance)

            instance.name = validated_data.get('name',instance.name)
            instance.accessory_model = validated_data.get('accessory_model',instance.accessory_model)
            instance.accessory_type = validated_data.get('accessory_type',instance.accessory_type)
            instance.manufacturer = validated_data.get('manufacturer',instance.manufacturer)
            instance.is_new = validated_data.get('is_new',instance.is_new)
            instance.is_our = validated_data.get('is_our',instance.is_our)
            instance.count = validated_data.get('count',instance.count)
            instance.rated_price = validated_data.get('rated_price',instance.rated_price)
            instance.entry_warehouse_date = validated_data.get('entry_warehouse_date',instance.entry_warehouse_date)
            instance.save()

            print("Accessory ID",instance.id)
            print("VALIDATED DATA",validated_data)
            validated_data.update({'accessory_id':instance.id})
            print("VALIDATED DATA NEWW",validated_data)
            accessory_history = AccessoryHistory.objects.create(**validated_data)

            return instance
