from django_filters import rest_framework as filter
from department.api.models import Department

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass

class DepartmentFilter(filter.FilterSet):
    name = filter.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Department
        fields = ['name','id']