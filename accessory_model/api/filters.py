from django_filters import rest_framework as filter
from accessory_model.api.models import AccessoryModel

class AccessoryModelFilter(filter.FilterSet):
    name = filter.CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = AccessoryModel
        fields=['id','name']