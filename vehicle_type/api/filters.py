from django_filters import rest_framework as filter
from vehicle_type.api.models import VehicleType

class VehicleTypeFilter(filter.FilterSet):
    name = filter.CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = VehicleType
        fields=['id','name']