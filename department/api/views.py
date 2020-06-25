from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from department.api.serializers import DepartmentSerializer
from department.api.models import Department
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from department.api.filters import DepartmentFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class DepartmentListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    filter_class = DepartmentFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class DepartmentUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    # permission_classes=[IsAuthenticated]