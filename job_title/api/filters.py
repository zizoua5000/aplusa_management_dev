from django_filters import rest_framework as filter
from job_title.api.models import JobTitle

class JobTitleFilter(filter.FilterSet):
    name = filter.CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = JobTitle
        fields=['id','name']