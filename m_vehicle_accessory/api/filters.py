from django_filters import rest_framework as filter
from m_vehicle_accessory.api.models import MVehicleAccessory

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass

class MVehicleAccessoryFilter(filter.FilterSet):
    vehicle = NumberInFilter(field_name='vehicle', lookup_expr='in') 
    accessory = NumberInFilter(field_name='accessory', lookup_expr='in')
    count = NumberInFilter(field_name ='count', lookup_expr='in') 

    class Meta:
        model = MVehicleAccessory
        fields = ['id','vehicle','accessory','count']

