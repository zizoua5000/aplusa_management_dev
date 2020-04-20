from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from company.api.serializers import CompanySerializer
from company.api.models import Company
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class CompanyListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    # permission_classes=[IsAuthenticated]

class CompanyUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    # permission_classes=[IsAuthenticated]