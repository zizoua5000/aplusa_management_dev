from django_filters import rest_framework as filter
from device.api.models import Device
from price.api.customfilter import DateListFilter


class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass
class CharInFilter(filter.BaseInFilter, filter.CharFilter):
    pass

class DeviceFilter(filter.FilterSet):
    id = NumberInFilter(field_name='id',lookup_expr='in')
    serie= CharInFilter(field_name='serie', lookup_expr='in')
    company = NumberInFilter(field_name='company', lookup_expr='in')
    device_model = NumberInFilter(field_name='device_model', lookup_expr='in')
    device_type = NumberInFilter(field_name='device_type', lookup_expr='in')
    device_mark = NumberInFilter(field_name ='device_model__device_mark', lookup_expr='in')
    status = NumberInFilter(field_name ='device_details__status', lookup_expr='in')
    simcard = NumberInFilter(field_name ='device_details__simcard', lookup_expr='in')
    package = NumberInFilter(field_name='device_details__simcard__package', lookup_expr='in') 
    has_rouming = filter.BooleanFilter(field_name='device_details__simcard__has_rouming')
    is_active = filter.BooleanFilter(field_name='device_details__simcard__is_active')
    company_vehicle = NumberInFilter(field_name ='device_details__company', lookup_expr='in')
    plate = CharInFilter(field_name ='device_details__vehicle__plate', lookup_expr='in')
    recipient = NumberInFilter(field_name ='device_details__recipient', lookup_expr='in')
    device_location = NumberInFilter(field_name ='device_details__device_location', lookup_expr='in')
    configuration = NumberInFilter(field_name ='device_details__configuration', lookup_expr='in')
    project = NumberInFilter(field_name ='device_details__project', lookup_expr='in')
    region = NumberInFilter(field_name ='device_details__region', lookup_expr='in')
    status_datetime = DateListFilter(field_name='device_details__status_datetime__date',lookup_expr='in')
    price_datetime = DateListFilter(field_name='device_details__price_datetime__date',lookup_expr='in')
    comment=filter.CharFilter(field_name ='device_details__comment',lookup_expr='icontains')

    class Meta:
        model = Device
        fields = ['serie','id','device_model','device_type','device_mark','status','company_vehicle',
        'simcard','simcard','plate','recipient','package','has_rouming','is_active','device_location',
        'configuration','project','region','comment','status_datetime','price_datetime']


