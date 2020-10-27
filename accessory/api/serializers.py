from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from accessory.api.models import Accessory
from accessory_history.api.models import AccessoryHistory
from accessory_model.api.serializers import AccessoryModelSerializer
from accessory_type.api.serializers import AccessoryTypeSerializer
from company.api.serializers import CompanySerializer
from accessory_history.api.serializers import AccessoryHistorySerializer


class AccessorySerializer(ModelSerializer):
        accessory_histories = AccessoryHistorySerializer(many=True)
        accessory_model_detail = SerializerMethodField()
        accessory_type_detail = SerializerMethodField()
        manufacturer_detail = SerializerMethodField()
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
                'accessory_histories',
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
            print("Count: ",validated_data.get('count'))

            accessory_count = validated_data.get('count')

            accessory_histories = validated_data.pop('accessory_histories')
            print("COUNT ", accessory_count)
            accessory = Accessory.objects.create(**validated_data)

            print("ACCESSORY ALL : ",validated_data)
            print("ACCESSORY HISTORY : ",accessory_histories)
            # print("Ordered Dict to dict : ",loads(dumps(accessory_histories)))
            rated_price = accessory_histories[0].get('rated_price')
            entry_warehouse_date = accessory_histories[0].get('entry_warehouse_date')
            acc_dict = {'add_count':accessory_count,'rated_price':rated_price,
            'accessory_id':accessory.id,'entry_warehouse_date':entry_warehouse_date}

            accessory_history = AccessoryHistory.objects.create(**acc_dict)  
            print("ACCESSORY History ALL : ",accessory_history)   
            return accessory     

        def update(self, instance, validated_data):
            print("INSTANCE",instance)
            print("VALIDATED DATA",validated_data)
            accessory_count = validated_data.get('count')

            accessory_histories = validated_data.pop('accessory_histories')
            print("AccEessory History",accessory_histories)
            accessory_histories_add_count = accessory_histories[0].get('add_count')
            rated_price = accessory_histories[0].get('rated_price')
            entry_warehouse_date = accessory_histories[0].get('entry_warehouse_date')

            if accessory_histories_add_count!=None:

                accessory_count += accessory_histories_add_count
                print("Accessory Histories ", accessory_histories)
                print("COUNT ", accessory_count)

                validated_data.update({'count':accessory_count})
                validated_data.update({'accessory_id':instance.id})
                print("VALIDATED DATA NEWW",validated_data)
                acc_dict_his = {'add_count':accessory_histories_add_count,'rated_price':rated_price,
                'accessory_id':instance.id,'entry_warehouse_date':entry_warehouse_date}

                accessory_history = AccessoryHistory.objects.create(**acc_dict_his)
        
            instance.name = validated_data.get('name',instance.name)
            instance.accessory_model = validated_data.get('accessory_model',instance.accessory_model)
            instance.accessory_type = validated_data.get('accessory_type',instance.accessory_type)
            instance.manufacturer = validated_data.get('manufacturer',instance.manufacturer)
            instance.is_new = validated_data.get('is_new',instance.is_new)
            instance.is_our = validated_data.get('is_our',instance.is_our)
            instance.count = validated_data.get('count',instance.count)
            instance.save()

            print("Accessory ID",instance.id)

            print("VALIDATED DATA",validated_data)
            return instance

