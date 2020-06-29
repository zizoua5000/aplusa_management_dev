from django_filters import rest_framework as filter
from configuration.api.models import Configuration

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass

class ConfigurationFilter(filter.FilterSet):
    name = filter.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Configuration
        fields = ['name','id']