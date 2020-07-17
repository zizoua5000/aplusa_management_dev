from django_filters import rest_framework as filter
from responsible_person.api.models import ResponsiblePerson

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass
class CharInFilter(filter.BaseInFilter, filter.CharFilter):
    pass

class ResponsiblePersonFilter(filter.FilterSet):
    id = NumberInFilter(field_name='id',lookup_expr='in')
    department = NumberInFilter(field_name='department', lookup_expr='in')
    department_chief = NumberInFilter(field_name='department_chief', lookup_expr='in')
    chief_substitute = NumberInFilter(field_name ='chief_substitute', lookup_expr='in')
    accounter = NumberInFilter(field_name='accounter', lookup_expr='in')
    recipient = NumberInFilter(field_name='recipient', lookup_expr='in')
    provider = NumberInFilter(field_name ='provider', lookup_expr='in')
    active = filter.BooleanFilter(field_name='active')

    class Meta:
        model = ResponsiblePerson
        fields = ['id','department','department_chief','chief_substitute','accounter',
        'recipient','provider','active']


