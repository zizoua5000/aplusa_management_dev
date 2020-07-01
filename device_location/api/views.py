from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from device_location.api.serializers import DeviceLocationSerializer
from device_location.api.models import DeviceLocation
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from device_location.api.filters import DeviceLocationFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class DeviceLocationListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=DeviceLocation.objects.all()
    serializer_class=DeviceLocationSerializer
    filter_backends = (filter.DjangoFilterBackend,filters.OrderingFilter)
    filter_class = DeviceLocationFilter
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class DeviceLocationUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=DeviceLocation.objects.all()
    serializer_class=DeviceLocationSerializer
    # permission_classes=[IsAuthenticated]