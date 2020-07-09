from django_filters import rest_framework as filter
from accessory_type.api.models import AccessoryType

class AccessoryTypeFilter(filter.FilterSet):
    name = filter.CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = AccessoryType
        fields=['id','name']