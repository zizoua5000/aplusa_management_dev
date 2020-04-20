from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from device_location.api.serializers import DeviceLocationSerializer
from device_location.api.models import DeviceLocation
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class DeviceLocationListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=DeviceLocation.objects.all()
    serializer_class=DeviceLocationSerializer
    # permission_classes=[IsAuthenticated]

class DeviceLocationUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=DeviceLocation.objects.all()
    serializer_class=DeviceLocationSerializer
    # permission_classes=[IsAuthenticated]