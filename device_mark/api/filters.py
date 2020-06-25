from django_filters import rest_framework as filter
from device_mark.api.models import DeviceMark

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass

class DeviceMarkFilter(filter.FilterSet):
    name = filter.CharFilter(lookup_expr='icontains') 

    class Meta:
        model = DeviceMark
        fields = ['name','id']

