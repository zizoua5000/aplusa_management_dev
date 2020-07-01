from django_filters import rest_framework as filter
from company.api.models import Company

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass
class CharInFilter(filter.BaseInFilter, filter.CharFilter):
    pass

class CompanyFilter(filter.FilterSet):
    # name = filter.CharFilter(lookup_expr='icontains')
    id = NumberInFilter(field_name='id',lookup_expr='in')
    name = CharInFilter(field_name='name',lookup_expr='in')
    company_type = NumberInFilter(field_name='company_type', lookup_expr='in') 
    main_company = NumberInFilter(field_name='main_company', lookup_expr='in') 
    
    class Meta:
        model = Company
        fields = ['name','company_type','main_company','id']