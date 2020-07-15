from django_filters import rest_framework as filter
from price.api.models import Price
from price.api.customfilter import DateListFilter

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass
class CharInFilter(filter.BaseInFilter, filter.CharFilter):
    pass

class PriceFilter(filter.FilterSet):
    id = NumberInFilter(field_name='id',lookup_expr='in')
    start_datetime = DateListFilter(field_name='start_datetime__date',lookup_expr='in')
    end_datetime = DateListFilter(field_name='end_datetime__date',lookup_expr='in')
    price_type = NumberInFilter(field_name='price_type',lookup_expr='in')
    sell_price = NumberInFilter(field_name='sell_price', lookup_expr='in') 
    project = NumberInFilter(field_name='project',lookup_expr='in')
    device_model = NumberInFilter(field_name='device_model', lookup_expr='in')
    accessory_model = NumberInFilter(field_name='accessory_model', lookup_expr='in')
    is_second_hand =  filter.BooleanFilter(field_name='is_second_hand')


    class Meta:
        model = Price
        fields = ['id','price_type','sell_price','project','device_model','accessory_model','is_second_hand','start_datetime','end_datetime']


