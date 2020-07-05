from django_filters import rest_framework as filter
from django.contrib.auth.models import Permission

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass
class CharInFilter(filter.BaseInFilter, filter.CharFilter):
    pass

class PermissionFilter(filter.FilterSet):
    id = NumberInFilter(field_name='id',lookup_expr='in')
    name = CharInFilter(field_name='name',lookup_expr='in')
    codename = CharInFilter(field_name='codename',lookup_expr='in')
    content_type = NumberInFilter(field_name='content_type', lookup_expr='in')

    class Meta:
        model = Permission
        fields = ['id','name','codename','content_type']


