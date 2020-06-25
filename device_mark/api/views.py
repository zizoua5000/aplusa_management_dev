from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from device_mark.api.serializers import DeviceMarkSerializer
from device_mark.api.models import DeviceMark
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from device_mark.api.filters import DeviceMarkFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class DeviceMarkListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=DeviceMark.objects.all()
    serializer_class=DeviceMarkSerializer
    filter_class = DeviceMarkFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class DeviceMarkUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=DeviceMark.objects.all()
    serializer_class=DeviceMarkSerializer
    # permission_classes=[IsAuthenticated]