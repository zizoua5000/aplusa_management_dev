from django_filters import rest_framework as filter
from company.api.models import Company

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass

class CompanyFilter(filter.FilterSet):
    name = filter.CharFilter(lookup_expr='icontains')
    company_type = NumberInFilter(field_name='company_type', lookup_expr='in') 
    main_company = NumberInFilter(field_name='main_company', lookup_expr='in') 
    
    class Meta:
        model = Company
        fields = ['name','company_type','main_company','id']