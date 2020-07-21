from django_filters import rest_framework as filter
from fw_version.api.models import FWVersion

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass

class FWVersionFilter(filter.FilterSet):
    name = filter.CharFilter(lookup_expr='icontains')

    class Meta:
        model = FWVersion
        fields = ['name','id']