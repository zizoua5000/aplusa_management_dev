from django_filters import rest_framework as filter
from device.api.customfilter import DateListFilter
from device.api.models import Device

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
    manufacturer = NumberInFilter(field_name='manufacturer', lookup_expr='in')
    status = NumberInFilter(field_name ='status', lookup_expr='in')
    simcard = NumberInFilter(field_name ='simcard', lookup_expr='in')
    package = NumberInFilter(field_name='simcard__package', lookup_expr='in') 
    has_rouming = filter.BooleanFilter(field_name='simcard__has_rouming')
    is_active = filter.BooleanFilter(field_name='simcard__is_active')
    # company_vehicle = NumberInFilter(field_name ='device_details__company', lookup_expr='in')
    plate = CharInFilter(field_name ='vehicle__plate', lookup_expr='in')
    recipient = NumberInFilter(field_name ='recipient', lookup_expr='in')
    device_location = NumberInFilter(field_name ='device_location', lookup_expr='in')
    configuration = NumberInFilter(field_name ='configuration', lookup_expr='in')
    fw_version = NumberInFilter(field_name ='fw_version', lookup_expr='in')
    project = NumberInFilter(field_name ='project', lookup_expr='in')
    sell_count = NumberInFilter(field_name='sell_count',lookup_expr='in')
    rated_price = NumberInFilter(field_name='rated_price',lookup_expr='in')
    guarantee_to_us = DateListFilter(field_name='guarantee_to_us',lookup_expr='in')
    guarantee_from_us = DateListFilter(field_name='guarantee_from_us',lookup_expr='in')
    manufacture_date = DateListFilter(field_name='manufacture_date',lookup_expr='in')
    buy_date = DateListFilter(field_name='buy_date',lookup_expr='in')
    entry_warehouse_date = DateListFilter(field_name='entry_warehouse_date',lookup_expr='in')
    device_event_datetime = DateListFilter(field_name='device_event_datetime',lookup_expr='in')
    webtrack_status = NumberInFilter(field_name ='webtrack_status', lookup_expr='in')
    is_our = filter.BooleanFilter(field_name='is_our')
    is_rent = filter.BooleanFilter(field_name='is_rent')
    is_sold = filter.BooleanFilter(field_name='is_sold')
    sell_price = NumberInFilter(field_name='sell_price',lookup_expr='in')
    comment=filter.CharFilter(field_name ='comment',lookup_expr='icontains')

    class Meta:
        model = Device
        fields = ['serie','id','device_model','device_type','device_mark','status','manufacturer',
        'simcard','plate','recipient','package','has_rouming','is_active','device_location',
        'configuration','fw_version','project','sell_count','rated_price','guarantee_to_us','guarantee_from_us','manufacture_date',
        'buy_date','entry_warehouse_date','device_event_datetime','webtrack_status','is_sold','is_rent','is_our','sell_price','comment']


