from django_filters import rest_framework as filter
from accessory.api.models import Accessory
from accessory.api.customfilter import DateListFilter

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass
class CharInFilter(filter.BaseInFilter, filter.CharFilter):
    pass

class AccessoryFilter(filter.FilterSet):
    id = NumberInFilter(field_name='id',lookup_expr='in')
    name = CharInFilter(field_name='name',lookup_expr='in')
    accessory_model = NumberInFilter(field_name='accessory_model', lookup_expr='in')
    accessory_type = NumberInFilter(field_name='accessory_type', lookup_expr='in')
    manufacturer = NumberInFilter(field_name='manufacturer', lookup_expr='in')
    count = NumberInFilter(field_name='count', lookup_expr='in')
    is_new = filter.BooleanFilter(field_name='is_new')
    is_new = filter.BooleanFilter(field_name='is_new')

    class Meta:
        model = Accessory
        fields = ['name','id','accessory_model','accessory_type','is_new','is_our','manufacturer','count']


