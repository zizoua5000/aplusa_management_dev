from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from vehicle.api.serializers import VehicleSerializer
from vehicle.api.models import Vehicle
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class VehicleListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Vehicle.objects.all()
    serializer_class=VehicleSerializer
    # permission_classes=[IsAuthenticated]

class VehicleUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Vehicle.objects.all()
    serializer_class=VehicleSerializer
    # permission_classes=[IsAuthenticated]