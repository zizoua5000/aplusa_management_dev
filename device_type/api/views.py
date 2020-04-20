from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from device_type.api.serializers import DeviceTypeSerializer
from device_type.api.models import DeviceType
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class DeviceTypeListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=DeviceType.objects.all()
    serializer_class=DeviceTypeSerializer
    # permission_classes=[IsAuthenticated]

class DeviceTypeUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=DeviceType.objects.all()
    serializer_class=DeviceTypeSerializer
    # permission_classes=[IsAuthenticated]