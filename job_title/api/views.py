from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from job_title.api.serializers import JobTitleSerializer
from job_title.api.models import JobTitle
from job_title.api.filters import JobTitleFilter
from rest_framework import filters
from django_filters import rest_framework as filter
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)



class JobTitleListCreateAPIView(ListCreateAPIView):  
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=JobTitle.objects.all().order_by('id')
    serializer_class=JobTitleSerializer
    filter_backends = (filter.DjangoFilterBackend,filters.OrderingFilter)
    filter_class = JobTitleFilter
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class JobTitleUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=JobTitle.objects.all()
    serializer_class=JobTitleSerializer
    # permission_classes=[IsAuthenticated]