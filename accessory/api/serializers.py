from rest_framework.serializers import ModelSerializer,SerializerMethodField,ValidationError
from rest_framework import serializers
from accessory.api.models import Accessory
from accessory_history.api.models import AccessoryHistory
from accessory_model.api.serializers import AccessoryModelSerializer
from accessory_type.api.serializers import AccessoryTypeSerializer
from company.api.serializers import CompanySerializer
from accessory_history.api.serializers import AccessoryHistorySerializer
from aplusa_management.static_values import *


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

        def validate(self, attrs):
            print("VALIDATE METHOD ") 
            print("ATTRS ", attrs)
            print(attrs['name'])
            # print(attrs['accessory_histories'][0]['rated_price'])
            print("SELF INSTANCE ", self.instance)
            checkDuplicateQuery = Accessory.objects.all().filter(name__exact=attrs['name'], manufacturer__exact=attrs['manufacturer'])
            if self.instance == None:
                # Validation for Create    
                if attrs['count']<0:
                    raise ValidationError('COUNT CAN NOT BE MINUS')
                else:        
                    if checkDuplicateQuery.exists():
                        raise ValidationError('THERE IS AN ACCESSORY WITH SELECTED NAME AND MANUFACTURER')
                    else:
                        if attrs['count']==0:
                            raise ValidationError('COUNT CAN NOT BE ZERO(0)')
                        else:
                            if attrs['is_our'] and attrs['is_new']:
                                if attrs['accessory_histories'][0]['rated_price']==None:
                                    raise ValidationError('RATED PRICE CAN NOT BE EMPTY')
                        return attrs
            else:
                # Validation for Update
                addCount = attrs['accessory_histories'][0]['add_count']
                count = attrs['count']
                rated_price = attrs['accessory_histories'][0]['rated_price']
                print('COUNT & ADDCOUNT', count,addCount)
                
                if checkDuplicateQuery.exists():
                    for item in checkDuplicateQuery:
                        print(item.accessory_model)
                        print(item.manufacturer)
                        if self.instance.name==item.name and self.instance.manufacturer==item.manufacturer:
                            print("SELF")
                            if addCount!= None:
                                if addCount==0:
                                    raise ValidationError('COUNT CAN NOT BE ZERO(0)')
                                else:
                                    if (count+addCount)<0:
                                        raise ValidationError('ACCESSORY COUNT CAN NOT BE MINUS')
                                    if attrs['is_our'] and attrs['is_new']: 
                                        if rated_price==None:
                                            raise ValidationError('RATED PRICE CAN NOT BE EMPTY')
                                    return attrs
                            else:
                                return attrs   
                        else:
                            raise ValidationError("THERE IS AN ACCESSORY WITH SELECTED NAME AND MANUFACTURER")
                else:
                    if addCount!= None:
                        if attrs['accessory_histories'][0]['add_count']==0:
                            raise ValidationError('COUNT CAN NOT BE ZERO(0)')
                        else:
                            if attrs['is_our'] and attrs['is_new']:
                                if rated_price==None:
                                    raise ValidationError('RATED PRICE CAN NOT BE EMPTY')
                    return attrs

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
            status_id = STATIC_STATUS_ENTRY_WAREHOUSE
            acc_dict = {'add_count':accessory_count,'rated_price':rated_price,
            'accessory_id':accessory.id,'entry_warehouse_date':entry_warehouse_date,'status_id':status_id}

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
            status_id = STATIC_STATUS_ENTRY_WAREHOUSE

            if accessory_histories_add_count!=None:

                accessory_count += accessory_histories_add_count
                print("Accessory Histories ", accessory_histories)
                print("COUNT ", accessory_count)

                validated_data.update({'count':accessory_count})
                validated_data.update({'accessory_id':instance.id})
                print("VALIDATED DATA NEWW",validated_data)
                acc_dict_his = {'add_count':accessory_histories_add_count,'rated_price':rated_price,
                'accessory_id':instance.id,'entry_warehouse_date':entry_warehouse_date, 'status_id': status_id}

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

