from django_filters import rest_framework as filter
from django.contrib.auth.models import ContentType

class NumberInFilter(filter.BaseInFilter, filter.NumberFilter,):
    pass
class CharInFilter(filter.BaseInFilter, filter.CharFilter):
    pass

class ContentTypeFilter(filter.FilterSet):
    id = NumberInFilter(field_name='id',lookup_expr='in')
    app_label = filter.CharFilter(field_name='app_label',lookup_expr='icontains')
    model = filter.CharFilter(field_name='model',lookup_expr='icontains')
    
    class Meta:
        model = ContentType
        fields=['id','app_label','model']