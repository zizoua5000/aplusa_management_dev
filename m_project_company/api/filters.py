from django_filters import rest_framework as filter
from m_project_company.api.models import MProjectCompany

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass

class MProjectCompanyFilter(filter.FilterSet):
    project = NumberInFilter(field_name='project', lookup_expr='in') 
    company = NumberInFilter(field_name='company', lookup_expr='in') 

    class Meta:
        model = MProjectCompany
        fields = ['project','company','id']

