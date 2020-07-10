from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from device.api.serializers import DeviceSerializer
from device.api.models import Device
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from device.api.filters import DeviceFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class DeviceListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Device.objects.all()
    serializer_class=DeviceSerializer
    filter_class = DeviceFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class DeviceUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Device.objects.all()
    serializer_class=DeviceSerializer
    # permission_classes=[IsAuthenticated]