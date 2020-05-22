from django_filters import rest_framework as filter
from vehicle_mark.api.models import VehicleMark

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass

class VehicleMarkFilter(filter.FilterSet):
    name = filter.CharFilter(lookup_expr='icontains') 

    class Meta:
        model = VehicleMark
        fields = ['name','id']

