from rest_framework.serializers import ModelSerializer,SerializerMethodField,ValidationError
from responsible_person.api.serializers import ResponsiblePersonSerializer
from person.api.serializers import PersonSerializer
from status.api.serializers import StatusSerializer
from qaime_detail.api.serializers import QaimeDetailListSerializer
from qaime.api.models import Qaime
from qaime_detail.api.models import QaimeDetail
from device.api.models import Device
from accessory.api.models import Accessory
from simcard.api.models import Simcard
from simcard_history.api.models import SimcardHistory
from device_history.api.models import DeviceHistory
from pending.api.models import Pending
from event.api.models import Event
from event_type.api.models import EventType
from action.api.models import Action
from aplusa_management.static_values import *
import collections

class QaimeListSerializer(ModelSerializer): 
        responsible_person_detail=SerializerMethodField()
        recipient_detail=SerializerMethodField()
        status_detail=SerializerMethodField()
        class Meta:
            model=Qaime
            fields=[
                'id',
                'name',
                'responsible_person',
                'responsible_person_detail',
                'recipient',
                'recipient_detail',
                'status',
                'status_detail',
                'qaime_type',
                'is_formal',
                'qaime_datetime',
                'comment',
                'created_at',
                'updated_at',
                ]
        def get_responsible_person_detail(self,obj):
            return ResponsiblePersonSerializer(obj.responsible_person).data 
        def get_recipient_detail(self,obj):
            return PersonSerializer(obj.recipient).data 
        def get_status_detail(self,obj):
            return StatusSerializer(obj.status).data 

class QaimeChangeStatusSerializer(ModelSerializer): 
    #  This Serializer for updating status of Qaime to "Completed"
    #  Method:PUT
        class Meta:
            model=Qaime
            fields=[
                'id'
                ]

        def update(self, instance, validated_data):
            instance.status_id=STATIC_STATUS_COMPLETED
            instance.save()
            return instance

        

class QaimeCreateSerializer(ModelSerializer):
    #  This Serializer for creating Qaime with the type of selling
    #  Method:POST
    #  Posted data should be:   
    # {
    #     "name":"String",
    #     "comment":"String|null"
    #     "responsible_person": "Integer",
    #     "recipient": "Integer",
    #     "qaime_type": 1,
    #     "status":11,
    #     "qaime_datetime": "Datetime",
    #     "qaime_details": [ "Array",        
    #         For device 
    #         {
    #         "device":"Integer",,
    #         "accessory":null,
    #         "simcard":"Integer|null",
    #         "project":"Integer",
    #         "company":"Integer",
    #         "count":1,
    #         "sold_or_rent":"Integer",
    #         "configuration":"Integer|null",
    #         "fw_version":"Integer|null"
    #         },
    #
    #         For accessory
    #         {
    #         "device":null,
    #         "accessory":"Integer",
    #         "project":"Integer",
    #         "company":"Integer",
    #         "count":"Integer",
    #         "is_new":"Integer",
    #         }
    #     ]
    # }
    qaime_details = QaimeDetailListSerializer(many=True)
    class Meta: 
        model = Qaime
        fields=[
                'id','name','responsible_person','recipient','qaime_type','status',
                'qaime_datetime','comment','qaime_details'
                ]
    
    def validate(self, attrs):
        qaime_details=attrs['qaime_details']
        device_list=[]
        simcard_list=[]
        print(qaime_details)
        for q_d in qaime_details:
            if('device' not in q_d):
                raise ValidationError('DEVICE KEY REQUIRED')
            if('accessory' not in q_d):
                raise ValidationError('ACCESSORY KEY REQUIRED')
            q_d_device=q_d['device']
            q_d_accessory=q_d['accessory']
            if(q_d_device!=None):
                if('simcard' not in q_d):
                    raise ValidationError('SIMCARD KEY REQUIRED')
                if('configuration' not in q_d):
                    raise ValidationError('CONFIGURATION KEY REQUIRED')
                if('fw_version' not in q_d):
                    raise ValidationError('FW_VERSION KEY REQUIRED')
                q_d_simcard=q_d['simcard']

                if(q_d_device.status_id!=STATIC_STATUS_READY_TO_SELL):
                    raise ValidationError('DEVICE NOT READY TO SELL')
                
                is_using_simcard_in_device=Device.objects.filter(simcard=q_d_simcard).first()
                if(is_using_simcard_in_device!=None):
                    raise ValidationError('SIMCARD ALREADY USING IN OTHER DEVICE')

                if(q_d_device.id in device_list):
                    raise ValidationError('SAME DEVICES CAN NOT SELLING TWICE IN ONE QAIME')
                else:
                    device_list.append(q_d_device.id)

                if(q_d_simcard!=None):
                    if(q_d_simcard.id in simcard_list):
                        raise ValidationError('SAME SIMCARDS CAN NOT USING TWICE IN ONE QAIME')
                    else:
                        simcard_list.append(q_d_simcard.id)
                
            if(q_d_accessory!=None):
                if(q_d_accessory.count==0):
                    raise ValidationError('ACCESSORY COUNT IS NOT ENOUGH')

                
        # raise ValidationError('OKKKKKKKKK')
        return attrs

    def create(self, validated_data): 
        # print("VALI DATA____________________")
        # print(validated_data)
        # print("VALI DATA____________________")
        qaime_details=validated_data.get('qaime_details')
        popped_qaime_details = validated_data.pop('qaime_details')
        qaime=Qaime.objects.create(**validated_data)
 
        if(qaime.qaime_type==STATIC_QAIME_TYPE_SELLING):
            #This is for selling qaime type
            for q_d in qaime_details:
                q_d['qaime']=qaime
                QaimeDetail.objects.create(**q_d)

                # QaimeDetail has 2 types
                #   1.QaimeDetail for devices
                #   2.QaimeDetail for accessories
                if(q_d['device']!=None):
                    # 1.QaimeDetail for devices
                    device=q_d['device']

                    # If simcard selected we have to handle this situation
                    if(q_d['simcard']!=None):
                        simcard=q_d['simcard']
                        simcard.is_active=STATIC_SIMCARD_ACTIVE
                        simcard.device=device
                        simcard.save()

                        simcard_history=SimcardHistory.objects.create(
                            simcard=simcard,
                            package=simcard.package,
                            has_rouming=simcard.has_rouming,
                            is_active=simcard.is_active,
                            device=simcard.device
                        )
                        device.simcard=simcard

                    device.project=q_d['project']
                    device.company=q_d['company']
                    device.status_id=STATIC_STATUS_READY_TO_INSTALL
                    device.device_event_datetime=qaime.qaime_datetime 
                    device.recipient=qaime.recipient
                    device.device_location_id=STATIC_DEVICE_LOCATION_AT_CUSTOMER
                    device.configuration=q_d['configuration']
                    device.fw_version=q_d['fw_version']
                    device.sell_count=device.sell_count+1
                    if(q_d['sold_or_rent']==STATIC_SOLD):
                        device.is_sold=1
                    else:
                        device.is_rent=1
                    device.save()

                    device_history=DeviceHistory.objects.create(
                        serie=device.serie,
                        company=device.company,
                        device_model=device.device_model,
                        device_type=device.device_type,
                        status=device.status,
                        simcard=device.simcard if device.simcard!=None else None,
                        vehicle=device.vehicle if device.vehicle!=None else None,
                        recipient=device.recipient,
                        device_location=device.device_location,
                        configuration=device.configuration if device.configuration!=None else None,
                        project=device.project,
                        fw_version=device.fw_version if device.fw_version!=None else None,
                        manufacturer=device.manufacturer,
                        sell_count=device.sell_count,
                        rated_price=device.rated_price,
                        guarantee_to_us=device.guarantee_to_us,
                        guarantee_from_us=device.guarantee_from_us,
                        sell_price=device.sell_price,
                        is_our=device.is_our,
                        is_rent=device.is_rent,
                        is_sold=device.is_sold,
                        manufacture_date=device.manufacture_date,
                        buy_date=device.buy_date,
                        entry_warehouse_date=device.entry_warehouse_date,
                        device_event_datetime=device.device_event_datetime,
                        comment=device.comment,
                        webtrack_status=device.webtrack_status,
                        device=device
                    )

                    Event.objects.create(
                        action_id=STATIC_ACTION_QAIME_SALES,
                        event_type_id=STATIC_EVENT_TYPE_DEVICE_STATUS_CHANGED,
                        device_history=device_history,
                        event_datetime=qaime.qaime_datetime
                    )

                    Event.objects.create(
                        action_id=STATIC_ACTION_QAIME_SALES,
                        event_type_id=STATIC_EVENT_TYPE_DEVICE_LOCATION_CHANGED,
                        device_history=device_history,
                        event_datetime=qaime.qaime_datetime
                    )

                    if(q_d['sold_or_rent']==STATIC_SOLD):
                        Event.objects.create(
                        action_id=STATIC_ACTION_QAIME_SALES,
                        event_type_id=STATIC_EVENT_TYPE_IS_SOLD_CHANGED,
                        device_history=device_history,
                        event_datetime=qaime.qaime_datetime
                        )
                    else:
                        Event.objects.create(
                        action_id=STATIC_ACTION_QAIME_SALES,
                        event_type_id=STATIC_EVENT_TYPE_IS_RENT_CHANGED,
                        device_history=device_history,
                        event_datetime=qaime.qaime_datetime
                        )
                    
                    Event.objects.create(
                        action_id=STATIC_ACTION_QAIME_SALES,
                        event_type_id=STATIC_EVENT_TYPE_PROJECT_CHANGED,
                        device_history=device_history,
                        event_datetime=qaime.qaime_datetime
                    )  

                    Event.objects.create(
                        action_id=STATIC_ACTION_QAIME_SALES,
                        event_type_id=STATIC_EVENT_TYPE_COMPANY_CHANGED,
                        device_history=device_history,
                        event_datetime=qaime.qaime_datetime
                    ) 

                    if(q_d['configuration']!=None):
                        Event.objects.create(
                            action_id=STATIC_ACTION_QAIME_SALES,
                            event_type_id=STATIC_EVENT_TYPE_CONFIGURATION_CHANGED,
                            device_history=device_history,
                            event_datetime=qaime.qaime_datetime
                        ) 
                    if(q_d['fw_version']!=None):
                        Event.objects.create(
                            action_id=STATIC_ACTION_QAIME_SALES,
                            event_type_id=STATIC_EVENT_TYPE_FW_VERSION_CHANGED,
                            device_history=device_history,
                            event_datetime=qaime.qaime_datetime
                        )
                   
                    if(q_d['simcard']!=None):
                        Event.objects.create(
                            action_id=STATIC_ACTION_QAIME_SALES,
                            event_type_id=STATIC_EVENT_TYPE_SIMCARD_IS_ACTIVE_CHANGED,
                            simcard_history=simcard_history,
                            event_datetime=qaime.qaime_datetime
                        )

                        Event.objects.create(
                            action_id=STATIC_ACTION_QAIME_SALES,
                            event_type_id=STATIC_EVENT_TYPE_SIMCARD_PLUGGED_CHANGED,
                            simcard_history=simcard_history,
                            event_datetime=qaime.qaime_datetime
                        )

                if(q_d['accessory']!=None):
                    # 2.QaimeDetail for accessories
                    accessory=q_d['accessory']
                    accessory.count=accessory.count-q_d['count']
                    accessory.save()

                Pending.objects.create(
                            accessory=q_d['accessory'],
                            device=q_d['device'],
                            count=q_d['count'],
                            recipient=qaime.recipient,
                            project=q_d['project'],
                            company=q_d['company'],
                            status_id=STATIC_STATUS_PENDING
                        )

                Event.objects.create(
                        action_id=STATIC_ACTION_QAIME_SALES,
                        event_type_id=STATIC_EVENT_TYPE_RECIPIENT_CHANGED,
                        qaime=qaime,
                        event_datetime=qaime.qaime_datetime
                    )
        return qaime

    def to_representation(self, instance):
        serializer = QaimeListSerializer(instance)
        return serializer.data

class QaimeCreateReturnSerializer(ModelSerializer):
    #  This Serializer for creating Qaime with the type of returning
    #  Method:POST
    #  Posted data should be:   
    # {
    #     "name":"String",
    #     "comment":"String|null"
    #     "responsible_person": "Integer",
    #     "recipient": "Integer",
    #     "qaime_type": 2,
    #     "status":11,
    #     "qaime_datetime": "Datetime",
    #     "qaime_details": [ "Array",        
    #         For device 
    #         {
    #         "device":"Integer",
    #         "accessory":null,
    #         "simcard":"Integer|null",
    #         "project":"Integer",
    #         "company":"Integer",
    #         "configuration":"Integer|null",
    #         "fw_version":"Integer|null",
    #         "sold_or_rent":"Integer",
    #         },
    
    #         For accessory
    #         {
    #         "device":null,
    #         "accessory":"Integer",
    #         "project":"Integer",
    #         "company":"Integer",
    #         "count":"Integer",
    #         "is_new":"Integer",
    #         }
    #     ]
    # }
    qaime_details = QaimeDetailListSerializer(many=True)
    class Meta: 
        model = Qaime
        fields=[
                'id','name','responsible_person','recipient','qaime_type','status',
                'qaime_datetime','comment','qaime_details'
                ]
    
    def validate(self, attrs):
        qaime_details=attrs['qaime_details']
        device_list=[]
        print(qaime_details)
        for q_d in qaime_details:
            if('device' not in q_d):
                raise ValidationError('DEVICE KEY REQUIRED')
            if('accessory' not in q_d):
                raise ValidationError('ACCESSORY KEY REQUIRED')
            q_d_device=q_d['device']
            q_d_accessory=q_d['accessory']
            if(q_d_device!=None):
                if(q_d_device.status_id==STATIC_STATUS_READY_TO_SELL):
                    raise ValidationError('THE DEVICE HAS NOT BEEN SOLD YET')
                if(q_d_device.id in device_list):
                    raise ValidationError('SAME DEVICES CAN NOT RETURNING TWICE IN ONE QAIME')
                else:
                    device_list.append(q_d_device.id)  
            if(q_d_accessory!=None):
                accessory=q_d['accessory']
                if(accessory.is_new==True):
                    accessory_pending=Pending.objects.filter(
                                accessory=accessory,
                                project=q_d['project'],
                                company=q_d['company'],
                                status_id=STATIC_STATUS_PENDING
                            ).last()     
                    if(accessory_pending.count<q_d['count']):
                        raise ValidationError('ACCESSORY COUNT NOT ENAUGH IN PENDING')

        # raise ValidationError('OKKKKKKKKK')
        return attrs

    def create(self, validated_data): 
        print("VALI DATA____________________")
        print(validated_data)
        print("VALI DATA____________________")
        qaime_details=validated_data.get('qaime_details')
        popped_qaime_details = validated_data.pop('qaime_details')
        qaime=Qaime.objects.create(**validated_data)
 
        if(qaime.qaime_type==STATIC_QAIME_TYPE_RETURN):
            #This is for returning qaime type
            for q_d in qaime_details:
                q_d['qaime']=qaime
                QaimeDetail.objects.create(**q_d)

                # QaimeDetail has 2 types
                #   1.QaimeDetail for devices
                #   2.QaimeDetail for accessories
                if(q_d['device']!=None):
                    # 1.QaimeDetail for devices
                    device=q_d['device']

                    # There is 2 option:
                    # 1.If device not installed yet, then we have to decrease(1) sell count and delete Pending data
                    # 2.If device already installed,then we have not change sell count  and Pending data
                    if(device.status_id==STATIC_STATUS_READY_TO_INSTALL):
                        device.sell_count=device.sell_count-1
                        Pending.objects.filter(
                            device=device,
                            project=device.project,
                            company=device.company,
                            status_id=STATIC_STATUS_PENDING
                        ).last().delete()

                    # If simcard selected we have to handle this situation
                    if(device.simcard!=None):
                        simcard=device.simcard
                        simcard.is_active=STATIC_SIMCARD_DEACTIVE
                        simcard.device=device
                        simcard.save()

                        simcard_history=SimcardHistory.objects.create(
                            simcard=simcard,
                            package=simcard.package,
                            has_rouming=simcard.has_rouming,
                            is_active=simcard.is_active,
                            device=simcard.device
                        )
                        device.simcard=None

                    device.project=None
                    device.company=None
                    device.status_id=STATIC_STATUS_READY_TO_SELL
                    device.device_event_datetime=qaime.qaime_datetime 
                    device.recipient=qaime.recipient
                    device.device_location_id=STATIC_DEVICE_LOCATION_AT_APLUSA_SECURITY_WAREHOUSE

                    if(q_d['sold_or_rent']==1):
                        device.is_sold=0
                    else:
                        device.is_rent=0                
                    device.save()

                    device_history=DeviceHistory.objects.create(
                        serie=device.serie,
                        company=device.company if device.company!=None else None,
                        device_model=device.device_model,
                        device_type=device.device_type,
                        status=device.status,
                        simcard=device.simcard if device.simcard!=None else None,
                        vehicle=device.vehicle if device.vehicle!=None else None,
                        recipient=device.recipient,
                        device_location=device.device_location,
                        configuration=device.configuration if device.configuration!=None else None,
                        project=device.project if device.project!=None else None,
                        fw_version=device.fw_version if device.fw_version!=None else None,
                        manufacturer=device.manufacturer,
                        sell_count=device.sell_count,
                        rated_price=device.rated_price,
                        guarantee_to_us=device.guarantee_to_us,
                        guarantee_from_us=device.guarantee_from_us,
                        sell_price=device.sell_price,
                        is_our=device.is_our,
                        is_rent=device.is_rent,
                        is_sold=device.is_sold,
                        manufacture_date=device.manufacture_date,
                        buy_date=device.buy_date,
                        entry_warehouse_date=device.entry_warehouse_date,
                        device_event_datetime=device.device_event_datetime,
                        comment=device.comment,
                        webtrack_status=device.webtrack_status,
                        device=device
                    )

                    Event.objects.create(
                        action_id=STATIC_ACTION_QAIME_RETURN,
                        event_type_id=STATIC_EVENT_TYPE_DEVICE_STATUS_CHANGED,
                        device_history=device_history,
                        event_datetime=qaime.qaime_datetime
                    )

                    Event.objects.create(
                        action_id=STATIC_ACTION_QAIME_RETURN,
                        event_type_id=STATIC_EVENT_TYPE_DEVICE_LOCATION_CHANGED,
                        device_history=device_history,
                        event_datetime=qaime.qaime_datetime
                    )

                    if(q_d['sold_or_rent']==1):
                        Event.objects.create(
                        action_id=STATIC_ACTION_QAIME_RETURN,
                        event_type_id=STATIC_EVENT_TYPE_IS_SOLD_CHANGED,
                        device_history=device_history,
                        event_datetime=qaime.qaime_datetime
                        )
                    else:
                        Event.objects.create(
                        action_id=STATIC_ACTION_QAIME_RETURN,
                        event_type_id=STATIC_EVENT_TYPE_IS_RENT_CHANGED,
                        device_history=device_history,
                        event_datetime=qaime.qaime_datetime
                        )
                    
                    Event.objects.create(
                        action_id=STATIC_ACTION_QAIME_RETURN,
                        event_type_id=STATIC_EVENT_TYPE_PROJECT_CHANGED,
                        device_history=device_history,
                        event_datetime=qaime.qaime_datetime
                    )  

                    Event.objects.create(
                        action_id=STATIC_ACTION_QAIME_RETURN,
                        event_type_id=STATIC_EVENT_TYPE_COMPANY_CHANGED,
                        device_history=device_history,
                        event_datetime=qaime.qaime_datetime
                    ) 

                   
                    if(q_d['simcard']!=None):
                        Event.objects.create(
                            action_id=STATIC_ACTION_QAIME_RETURN,
                            event_type_id=STATIC_EVENT_TYPE_SIMCARD_IS_ACTIVE_CHANGED,
                            simcard_history=simcard_history,
                            event_datetime=qaime.qaime_datetime
                        )

                        Event.objects.create(
                            action_id=STATIC_ACTION_QAIME_RETURN,
                            event_type_id=STATIC_EVENT_TYPE_SIMCARD_UNPLUGGED_CHANGED,
                            simcard_history=simcard_history,
                            event_datetime=qaime.qaime_datetime
                        )

                if(q_d['accessory']!=None):
                    # 2.QaimeDetail for accessories
                    accessory=q_d['accessory']
                    accessory.count=accessory.count+q_d['count']
                    accessory.save()

                    # There is 2 option:
                    # 1.If accessory not installed yet(if accessory is_new=True), then we have to delete Pending data
                    # 2.If accessory already installed(if accessory is_new=False),then we have NOT delete Pending data
                    if(accessory.is_new==True):
                        accessory_pending=Pending.objects.filter(
                                accessory=q_d['accessory'],
                                project=q_d['project'],
                                company=q_d['company'],
                                status_id=STATIC_STATUS_PENDING
                            ).last()
                        if(accessory_pending.count==q_d['count']):
                            accessory_pending.delete()
                        elif(accessory_pending.count>q_d['count']):
                            accessory_pending.count=accessory_pending.count-q_d['count']
                            accessory_pending.save()

                Event.objects.create(
                        action_id=STATIC_ACTION_QAIME_RETURN,
                        event_type_id=STATIC_EVENT_TYPE_RECIPIENT_CHANGED,
                        qaime=qaime,
                        event_datetime=qaime.qaime_datetime
                    )
        return qaime

    def to_representation(self, instance):
        serializer = QaimeListSerializer(instance)
        return serializer.data



class QaimeDetailSerializer(ModelSerializer): 
        responsible_person_detail=SerializerMethodField()
        recipient_detail=SerializerMethodField()
        status_detail=SerializerMethodField()
        qaime_details_detail=SerializerMethodField()
        class Meta:
            model=Qaime
            fields=[
                'id',
                'name',
                'qaime_details_detail',
                'responsible_person',
                'responsible_person_detail',
                'recipient',
                'recipient_detail',
                'status',
                'status_detail',
                'qaime_type',
                'is_formal',
                'qaime_datetime',
                'comment',
                'created_at',
                'updated_at',
                ]
        def get_responsible_person_detail(self,obj):
            return ResponsiblePersonSerializer(obj.responsible_person).data 
        def get_recipient_detail(self,obj):
            return PersonSerializer(obj.recipient).data
        def get_qaime_details_detail(self,obj):
            return QaimeDetailListSerializer(QaimeDetail.objects.filter(qaime=obj), many=True).data
        def get_status_detail(self,obj):
            return StatusSerializer(obj.status).data
