from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from company_type.api.serializers import CompanyTypeSerializer
from company_type.api.models import CompanyType
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class CompanyTypeListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=CompanyType.objects.all()
    serializer_class=CompanyTypeSerializer
    # permission_classes=[IsAuthenticated]

class CompanyTypeUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=CompanyType.objects.all()
    serializer_class=CompanyTypeSerializer
    # permission_classes=[IsAuthenticated]