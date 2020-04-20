from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from device.api.serializers import DeviceSerializer
from device.api.models import Device
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class DeviceListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Device.objects.all()
    serializer_class=DeviceSerializer
    # permission_classes=[IsAuthenticated]

class DeviceUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Device.objects.all()
    serializer_class=DeviceSerializer
    # permission_classes=[IsAuthenticated]