from django_filters import rest_framework as filter
from accessory_history.api.models import AccessoryHistory
from accessory.api.customfilter import DateListFilter

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass
class CharInFilter(filter.BaseInFilter, filter.CharFilter):
    pass

class AccessoryHistoryFilter(filter.FilterSet):
    id = NumberInFilter(field_name='id',lookup_expr='in')
    name = CharInFilter(field_name='name',lookup_expr='in')
    accessory_model = NumberInFilter(field_name='accessory_model', lookup_expr='in')
    accessory_type = NumberInFilter(field_name='accessory_type', lookup_expr='in')
    manufacturer = NumberInFilter(field_name='manufacturer', lookup_expr='in')
    count = NumberInFilter(field_name='count', lookup_expr='in')
    rated_price = NumberInFilter(field_name='rated_price',lookup_expr='in')
    entry_warehouse_date = DateListFilter(field_name='entry_warehouse_date',lookup_expr='in')
    is_new = filter.BooleanFilter(field_name='is_new')
    is_new = filter.BooleanFilter(field_name='is_new')

    class Meta:
        model = AccessoryHistory
        fields = ['name','id','accessory_model','accessory_type','is_new','is_our','manufacturer','count']


