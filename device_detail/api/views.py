from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from device_detail.api.serializers import DeviceDetailSerializer
from device_detail.api.models import DeviceDetail
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class DeviceDetailListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=DeviceDetail.objects.all()
    serializer_class=DeviceDetailSerializer
    # permission_classes=[IsAuthenticated]

class DeviceDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=DeviceDetail.objects.all()
    serializer_class=DeviceDetailSerializer
    # permission_classes=[IsAuthenticated]