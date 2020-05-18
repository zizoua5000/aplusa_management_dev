import django_filters
from rest_framework import filters
from django_filters import Filter, FilterSet
from vehicle_model.api.models import VehicleModel
from django_filters.fields import Lookup

class NumberInFilter(django_filters.BaseInFilter, django_filters.NumberFilter,):
    pass

class VehicleModelFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    vehicle_mark = NumberInFilter(field_name='vehicle_mark', lookup_expr='in') 

    class Meta:
        model = VehicleModel
        fields = ['name','vehicle_mark','id']
 
