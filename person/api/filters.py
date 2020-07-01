from django_filters import rest_framework as filter
from person.api.models import Person

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass
class CharInFilter(filter.BaseInFilter, filter.CharFilter):
    pass

class PersonFilter(filter.FilterSet):
    id = NumberInFilter(field_name='id',lookup_expr='in')
    first_name = CharInFilter(field_name='first_name',lookup_expr='in')
    last_name = CharInFilter(field_name='last_name',lookup_expr='in')
    phone = CharInFilter(field_name='phone',lookup_expr='in')
    email = CharInFilter(field_name='email',lookup_expr='in')
    company = NumberInFilter(field_name='company', lookup_expr='in')
    department = NumberInFilter(field_name='department', lookup_expr='in')
    job_title = NumberInFilter(field_name='job_title', lookup_expr='in')
    user = NumberInFilter(field_name='user', lookup_expr='in')
    username = CharInFilter(field_name ='user__username', lookup_expr='in')
    is_active = filter.BooleanFilter(field_name='user__is_active')

    class Meta:
        model = Person
        fields = ['id','first_name','last_name','phone','email',
        'company','department','job_title','user','username','is_active']


