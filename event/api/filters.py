from django_filters import rest_framework as filter
from event.api.models import Event
from event.api.customfilter import DateListFilter

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass
class CharInFilter(filter.BaseInFilter, filter.CharFilter):
    pass

class EventFilter(filter.FilterSet):
    id = NumberInFilter(field_name='id',lookup_expr='in')
    action = NumberInFilter(field_name='action', lookup_expr='in')
    event_type = NumberInFilter(field_name='event_type', lookup_expr='in')
    device_history = NumberInFilter(field_name='device_history', lookup_expr='in')
    accessory_history = NumberInFilter(field_name='accessory_history', lookup_expr='in')
    accessory_fixing = NumberInFilter(field_name='accessory_fixing', lookup_expr='in')
    simcard_history = NumberInFilter(field_name='simcard_history', lookup_expr='in')
    event_region = NumberInFilter(field_name='event_region', lookup_expr='in')
    event_datetime = DateListFilter(field_name='event_datetime',lookup_expr='in')
    event_price = NumberInFilter(field_name='event_price', lookup_expr='in')
    comment = filter.CharFilter(field_name ='comment',lookup_expr='icontain')
    class Meta:
        model = Event
        fields=['id','action','event_type','device_history','accessory_history','accessory_fixing',
        'simcard_history','event_region','event_datetime','event_price','comment']