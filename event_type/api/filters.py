from django_filters import rest_framework as filter
from event_type.api.models import EventType

class EventTypeFilter(filter.FilterSet):
    name = filter.CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = EventType
        fields=['id','name']