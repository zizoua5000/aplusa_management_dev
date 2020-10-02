from django_filters import rest_framework as filter
from currency_rate.api.models import CurrencyRate
from currency_rate.api.customfilter import DateListFilter

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass
class CharInFilter(filter.BaseInFilter, filter.CharFilter):
    pass

class CurrencyRateFilter(filter.FilterSet):
    id = NumberInFilter(field_name='id',lookup_expr='in')
    start_date = DateListFilter(field_name='start_date',lookup_expr='in')
    end_date = DateListFilter(field_name='end_date',lookup_expr='in')
    rate = NumberInFilter(field_name='rate', lookup_expr='in')
    class Meta:
        model = CurrencyRate
        fields=['id','start_date','end_date','rate']