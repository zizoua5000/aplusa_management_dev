from django_filters import rest_framework as filter
from device_model.api.models import DeviceModel

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass

class DeviceModelFilter(filter.FilterSet):
    name = filter.CharFilter(lookup_expr='icontains')
    device_mark = NumberInFilter(field_name='device_mark', lookup_expr='in') 

    class Meta:
        model = DeviceModel
        fields = ['name','device_mark','id']

