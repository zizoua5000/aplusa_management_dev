from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from m_event_accessory.api.models import MEventAccessory
from event.api.serializers import EventSerializer
from accessory.api.serializers import AccessorySerializer
from person.api.serializers import PersonSerializer

class MEventAccessorySerializer(ModelSerializer):
        event_detail=SerializerMethodField()
        accessory_detail=SerializerMethodField()
        recipient_detail=SerializerMethodField()
        class Meta:
            model=MEventAccessory
            fields=['id','event','event_detail','accessory','accessory_detail','count','sell_price',
            'recipient','recipient_detail']

        def get_event_detail(self,obj):
            return EventSerializer(obj.event).data
        def get_accessory_detail(self,obj):
            return AccessorySerializer(obj.accessory).data
        def get_recipient_detail(self,obj):
            return PersonSerializer(obj.recipient).data            
