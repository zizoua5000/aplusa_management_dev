from django_filters import rest_framework as filter
from device_location.api.models import DeviceLocation

class DeviceLocationFilter(filter.FilterSet):
    name = filter.CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = DeviceLocation
        fields=['id','name']