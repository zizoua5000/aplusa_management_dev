from django_filters import rest_framework as filter
from device_type.api.models import DeviceType

class DeviceTypeFilter(filter.FilterSet):
    name = filter.CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = DeviceType
        fields=['id','name']