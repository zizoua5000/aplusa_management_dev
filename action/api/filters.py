from django_filters import rest_framework as filter
from action.api.models import Action

class ActionFilter(filter.FilterSet):
    name = filter.CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = Action
        fields=['id','name']