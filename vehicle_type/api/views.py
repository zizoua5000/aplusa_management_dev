from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from vehicle_type.api.serializers import VehicleTypeSerializer
from vehicle_type.api.models import VehicleType
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class VehicleTypeListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=VehicleType.objects.all()
    serializer_class=VehicleTypeSerializer
    # permission_classes=[IsAuthenticated]

class VehicleTypeUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=VehicleType.objects.all()
    serializer_class=VehicleTypeSerializer
    # permission_classes=[IsAuthenticated]