from rest_framework.serializers import ModelSerializer,SerializerMethodField
from event.api.models import Event
from action.api.serializers import ActionSerializer
from event_type.api.serializers import EventTypeSerializer
from device_history.api.serializers import DeviceHistorySerializer
from accessory_history.api.serializers import AccessoryHistorySerializer
from accessory_fixing.api.serializers import AccessoryFixingSerializer
from simcard_history.api.serializers import SimcardHistorySerializer
from region.api.serializers import RegionSerializer
from qaime.api.serializers import QaimeListSerializer

class EventSerializer(ModelSerializer):
        action_detail=SerializerMethodField()
        event_type_detail=SerializerMethodField()
        device_history_detail=SerializerMethodField()
        accessory_history_detail=SerializerMethodField()
        accessory_fixing_detail=SerializerMethodField()
        simcard_history_detail=SerializerMethodField()
        event_region_detail=SerializerMethodField()
        qaime=SerializerMethodField()

        class Meta:
            model=Event
            fields=['id','action','action_detail','event_type','event_type_detail','device_history','device_history_detail',
            'accessory_history','accessory_history_detail','accessory_fixing','accessory_fixing_detail',
            'simcard_history','simcard_history_detail','event_region','event_region_detail','qaime','qaime_detail','event_datetime','event_price','comment','created_at']

        def get_action_detail(self,obj):
            return ActionSerializer(obj.action).data
        def get_event_type_detail(self,obj):
            return EventTypeSerializer(obj.event_type).data            
        def get_device_history_detail(self,obj):
            return DeviceHistorySerializer(obj.device_history).data
        def get_accessory_history_detail(self,obj):
            return AccessoryHistorySerializer(obj.accessory_history).data
        def get_accessory_fixing_detail(self,obj):
            return AccessoryFixingSerializer(obj.accessory_fixing).data
        def get_simcard_history_detail(self,obj):
            return SimcardHistorySerializer(obj.simcard_history).data
        def get_event_region_detail(self,obj):
            return RegionSerializer(obj.event_region).data   
        def get_event_qaime_detail(self,obj):
            return QaimeListSerializer(obj.qaime).data          

