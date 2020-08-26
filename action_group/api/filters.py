from django_filters import rest_framework as filter
from action_group.api.models import ActionGroup

class ActionGroupFilter(filter.FilterSet):
    name = filter.CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = ActionGroup
        fields=['id','name']