from django_filters import rest_framework as filter
from django.contrib.auth.models import User

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass
class CharInFilter(filter.BaseInFilter, filter.CharFilter):
    pass

class UserPermissionFilter(filter.FilterSet):
    id = NumberInFilter(field_name='id',lookup_expr='in')
    username = CharInFilter(field_name='username', lookup_expr='in')
  
    class Meta:
        model = User
        fields = ['id','username']