from django_filters import rest_framework as filter
from region.api.models import Region

class RegionFilter(filter.FilterSet):
    name = filter.CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = Region
        fields=['id','name']