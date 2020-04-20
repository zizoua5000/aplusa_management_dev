from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from department.api.serializers import DepartmentSerializer
from department.api.models import Department
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class DepartmentListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    # permission_classes=[IsAuthenticated]

class DepartmentUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    # permission_classes=[IsAuthenticated]