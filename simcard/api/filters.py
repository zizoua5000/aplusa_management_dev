from django_filters import rest_framework as filter
from simcard.api.models import Simcard

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass
class CharInFilter(filter.BaseInFilter, filter.CharFilter):
    pass

class SimcardFilter(filter.FilterSet):
    id = NumberInFilter(field_name='id',lookup_expr='in')
    number = CharInFilter(field_name='number',lookup_expr='in')
    package = NumberInFilter(field_name='package', lookup_expr='in') 
    has_rouming = filter.BooleanFilter(field_name='has_rouming')
    is_active = filter.BooleanFilter(field_name='is_active')


    class Meta:
        model = Simcard
        fields = ['number','package','id','has_rouming','is_active']


