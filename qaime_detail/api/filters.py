from django_filters import rest_framework as filter
from qaime_detail.api.models import QaimeDetail
from qaime_detail.api.customfilter import DateListFilter

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass
class CharInFilter(filter.BaseInFilter, filter.CharFilter):
    pass
class QaimeDetailFilter(filter.FilterSet):
    qaime = NumberInFilter(field_name='qaime',lookup_expr='in')
    device = NumberInFilter(field_name='device',lookup_expr='in')
    accessory = NumberInFilter(field_name='accessory',lookup_expr='in')
    simcard = NumberInFilter(field_name='simcard',lookup_expr='in')
    project = NumberInFilter(field_name='project',lookup_expr='in')
    company = NumberInFilter(field_name='company',lookup_expr='in')
    configuration = NumberInFilter(field_name='configuration',lookup_expr='in')
    fw_version = NumberInFilter(field_name='fw_version',lookup_expr='in')
    count = NumberInFilter(field_name='count', lookup_expr='in')
    is_new = filter.BooleanFilter(field_name='is_new')

    class Meta:
        model = QaimeDetail
        fields = ['qaime','device','accessory','simcard','project','company','configuration','fw_version','count','is_new']

