from django_filters import rest_framework as filter
from accessory.api.models import Accessory

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass
class CharInFilter(filter.BaseInFilter, filter.CharFilter):
    pass

class AccessoryFilter(filter.FilterSet):
    id = NumberInFilter(field_name='id',lookup_expr='in')
    name = CharInFilter(field_name='name',lookup_expr='in')
    accessory_model = NumberInFilter(field_name='accessory_model', lookup_expr='in')
    accessory_type = NumberInFilter(field_name='accessory_type', lookup_expr='in')
    company = NumberInFilter(field_name ='company', lookup_expr='in')

    class Meta:
        model = Accessory
        fields = ['name','id','accessory_model','accessory_type','company']


