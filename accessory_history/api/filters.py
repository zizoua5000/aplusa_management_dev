from django_filters import rest_framework as filter
from accessory_history.api.models import AccessoryHistory

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass
class CharInFilter(filter.BaseInFilter, filter.CharFilter):
    pass

class AccessoryHistoryFilter(filter.FilterSet):
    id = NumberInFilter(field_name='id',lookup_expr='in')
    accessory_id = NumberInFilter(field_name='accessory_id',lookup_expr='in')
    manufacturer_id = NumberInFilter(field_name='manufacturer_id', lookup_expr='in')
    rated_price = NumberInFilter(field_name='rated_price', lookup_expr='in')
    count = NumberInFilter(field_name ='count', lookup_expr='in')

    class Meta:
        model = AccessoryHistory
        fields = ['id','accessory_id','manufacturer_id','rated_price','count']


