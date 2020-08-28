from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from m_project_company.api.serializers import MProjectCompanySerializer
from m_project_company.api.models import MProjectCompany
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from m_project_company.api.filters import MProjectCompanyFilter
from rest_framework import filters
from django_filters import rest_framework as filter

# from aplusa_management.filters import MProjectCompanyFilter
# from rest_framework import filters
# import django_filters


class MProjectCompanyListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=MProjectCompany.objects.all().order_by('id')
    serializer_class=MProjectCompanySerializer
    filter_class = MProjectCompanyFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    

class MProjectCompanyUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=MProjectCompany.objects.all().order_by('id')
    serializer_class=MProjectCompanySerializer
   
    
