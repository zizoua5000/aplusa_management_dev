from django_filters import rest_framework as filter
from vehicle_model.api.models import VehicleModel

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass

class VehicleModelFilter(filter.FilterSet):
    name = filter.CharFilter(lookup_expr='icontains')
    vehicle_mark = NumberInFilter(field_name='vehicle_mark', lookup_expr='in') 

    class Meta:
        model = VehicleModel
        fields = ['name','vehicle_mark','id']

