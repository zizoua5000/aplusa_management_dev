from django_filters import rest_framework as filter
from qaime.api.models import Qaime
from qaime.api.customfilter import DateListFilter

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass
class CharInFilter(filter.BaseInFilter, filter.CharFilter):
    pass
class QaimeFilter(filter.FilterSet):
    name = filter.CharFilter(field_name='name',lookup_expr='icontains')
    responsible_person = NumberInFilter(field_name='responsible_person',lookup_expr='in')
    recipient = NumberInFilter(field_name='recipient',lookup_expr='in')
    qaime_type = NumberInFilter(field_name='qaime_type',lookup_expr='in')
    status = NumberInFilter(field_name='status',lookup_expr='in')
    is_formal = filter.BooleanFilter(field_name='is_formal')
    qaime_datetime = DateListFilter(field_name='qaime_datetime__date',lookup_expr='in')
    comment = filter.CharFilter(field_name ='comment',lookup_expr='icontains')
    class Meta:
        model = Qaime
        fields = ['name','id']

