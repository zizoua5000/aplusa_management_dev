import django_filters
from vehicle_model.api.models import VehicleModel

class VehicleModelFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = VehicleModel
        fields = ['name','vehicle_mark']
