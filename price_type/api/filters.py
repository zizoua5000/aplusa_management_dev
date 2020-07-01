from django_filters import rest_framework as filter
from price_type.api.models import PriceType

class PriceTypeFilter(filter.FilterSet):
    name = filter.CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = PriceType
        fields=['id','name']