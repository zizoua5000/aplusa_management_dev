from django_filters import rest_framework as filter
from accessory_history.api.models import AccessoryHistory
from accessory_history.api.customfilter import DateListFilter

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass
class CharInFilter(filter.BaseInFilter, filter.CharFilter):
    pass

class AccessoryHistoryFilter(filter.FilterSet):

    id = NumberInFilter(field_name='id',lookup_expr='in')
    accessory = NumberInFilter(field_name='accessory',lookup_expr='in')
    add_count = NumberInFilter(field_name='add_count', lookup_expr='in')
    rated_price = NumberInFilter(field_name='rated_price',lookup_expr='in')
    entry_warehouse_date = DateListFilter(field_name='entry_warehouse_date',lookup_expr='in')
    class Meta:
        model = AccessoryHistory
        fields = ['rated_price','id','add_count','accessory','entry_warehouse_date']


