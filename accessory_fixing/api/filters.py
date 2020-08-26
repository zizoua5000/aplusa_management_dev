from django_filters import rest_framework as filter
from accessory_fixing.api.models import AccessoryFixing
from accessory_fixing.api.customfilter import DateListFilter

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass
class CharInFilter(filter.BaseInFilter, filter.CharFilter):
    pass

class AccessoryFixingFilter(filter.FilterSet):
    id = NumberInFilter(field_name='id',lookup_expr='in')
    accessory_id = NumberInFilter(field_name='accessory_id',lookup_expr='in')
    company_id = NumberInFilter(field_name='company_id', lookup_expr='in')
    vehicle_id = NumberInFilter(field_name='vehicle_id',lookup_expr='in')
    accessory_status_id = NumberInFilter(field_name='accessory_status_id', lookup_expr='in')
    accessory_event_datetime = DateListFilter(field_name='date',lookup_expr='in')
    comment=filter.CharFilter(field_name ='comment',lookup_expr='icontains')

    class Meta:
        model = AccessoryFixing
        fields = ['id','accessory_id','company_id','vehicle_id','accessory_status_id','accessory_event_datetime','comment']


