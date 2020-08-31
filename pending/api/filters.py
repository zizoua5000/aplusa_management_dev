from django_filters import rest_framework as filter
from pending.api.models import Pending

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass

class PendingFilter(filter.FilterSet):
    project = NumberInFilter(field_name='project', lookup_expr='in') 
    company = NumberInFilter(field_name='company', lookup_expr='in') 
    accessory = NumberInFilter(field_name='accessory', lookup_expr='in') 
    recipient = NumberInFilter(field_name='recipient', lookup_expr='in') 
    status = NumberInFilter(field_name='status', lookup_expr='in') 
    count = NumberInFilter(field_name='count', lookup_expr='in') 
    device = NumberInFilter(field_name='device', lookup_expr='in') 
    class Meta:
        model = Pending
        fields = ['project','company','id','accessory','recipient','status','count','device']

