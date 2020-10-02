from django_filters import rest_framework as filter
from m_event_person.api.models import MEventPerson

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass

class MEventPersonFilter(filter.FilterSet):
    event = NumberInFilter(field_name='event', lookup_expr='in') 
    person = NumberInFilter(field_name ='person', lookup_expr='in')

    class Meta:
        model = MEventPerson
        fields = ['id','event','person',]

