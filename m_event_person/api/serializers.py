from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from m_event_person.api.models import MEventPerson
from event.api.serializers import EventSerializer
from person.api.serializers import PersonSerializer

class MEventPersonSerializer(ModelSerializer):
        event_detail=SerializerMethodField()
        person_detail=SerializerMethodField()
        class Meta:
            model=MEventPerson
            fields=['id','event','event_detail','person','person_detail',]

        def get_event_detail(self,obj):
            return EventSerializer(obj.event).data
        def get_person_detail(self,obj):
            return PersonSerializer(obj.person).data           
