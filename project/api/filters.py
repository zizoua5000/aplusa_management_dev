from django_filters import rest_framework as filter
from project.api.models import Project

class ProjectFilter(filter.FilterSet):
    name = filter.CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = Project
        fields=['id','name']