from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from device_model.api.serializers import DeviceModelSerializer
from device_model.api.models import DeviceModel
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class DeviceModelListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=DeviceModel.objects.all()
    serializer_class=DeviceModelSerializer
    # permission_classes=[IsAuthenticated]

class DeviceModelUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=DeviceModel.objects.all()
    serializer_class=DeviceModelSerializer
    # permission_classes=[IsAuthenticated]