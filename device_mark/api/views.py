from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from device_mark.api.serializers import DeviceMarkSerializer
from device_mark.api.models import DeviceMark
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class DeviceMarkListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=DeviceMark.objects.all()
    serializer_class=DeviceMarkSerializer
    # permission_classes=[IsAuthenticated]

class DeviceMarkUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=DeviceMark.objects.all()
    serializer_class=DeviceMarkSerializer
    # permission_classes=[IsAuthenticated]