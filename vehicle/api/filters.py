from django_filters import rest_framework as filter
from vehicle.api.models import Vehicle

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass

class VehicleFilter(filter.FilterSet):
    plate = filter.CharFilter(field_name='plate',lookup_expr='iexact')
    serie_number = filter.CharFilter(field_name='serie_number', lookup_expr='iexact') 

    class Meta:
        model = Vehicle
        fields = ['plate','serie_number','id']

