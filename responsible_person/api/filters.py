from django_filters import rest_framework as filter
from vehicle.api.models import Vehicle

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass
class CharInFilter(filter.BaseInFilter, filter.CharFilter):
    pass

class VehicleFilter(filter.FilterSet):
    id = NumberInFilter(field_name='id',lookup_expr='in')
    plate = CharInFilter(field_name='plate',lookup_expr='in')
    serie_number = CharInFilter(field_name='serie_number', lookup_expr='in') 
    comment = filter.CharFilter(lookup_expr='icontains')
    vehicle_model = NumberInFilter(field_name='vehicle_model', lookup_expr='in')
    vehicle_type = NumberInFilter(field_name='vehicle_type', lookup_expr='in')
    vehicle_mark = NumberInFilter(field_name ='vehicle_model__vehicle_mark', lookup_expr='in')

    class Meta:
        model = Vehicle
        fields = ['plate','serie_number','id','comment','vehicle_model','vehicle_type','vehicle_mark']


