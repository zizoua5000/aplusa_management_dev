from django_filters import rest_framework as filter
from company_type.api.models import CompanyType

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass

class CompanyTypeFilter(filter.FilterSet):
    name = filter.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CompanyType
        fields = ['name','id']