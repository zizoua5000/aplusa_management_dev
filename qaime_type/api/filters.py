from django_filters import rest_framework as filter
from qaime_type.api.models import QaimeType

class QaimeTypeFilter(filter.FilterSet):
    name = filter.CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = QaimeType
        fields=['id','name']