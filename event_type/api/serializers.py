from rest_framework.serializers import ModelSerializer
from event_type.api.models import EventType

class EventTypeSerializer(ModelSerializer):
        class Meta:
            model=EventType
            fields=['id','name','created_at','updated_at']



