from django_filters import rest_framework as filter
from m_event_accessory.api.models import MEventAccessory

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass

class MEventAccessoryFilter(filter.FilterSet):
    event = NumberInFilter(field_name='event', lookup_expr='in') 
    accessory = NumberInFilter(field_name='accessory', lookup_expr='in')
    count = NumberInFilter(field_name ='count', lookup_expr='in') 
    sell_price = NumberInFilter(field_name='sell_price',lookup_expr='in')
    recipient = NumberInFilter(field_name ='recipient', lookup_expr='in')

    class Meta:
        model = MEventAccessory
        fields = ['id','event','accessory','count','sell_price','recipient',]

