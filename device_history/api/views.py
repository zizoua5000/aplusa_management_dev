from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from device_history.api.serializers import DeviceHistorySerializer
from device_history.api.models import DeviceHistory
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from device_history.api.filters import DeviceHistoryFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class DeviceHistoryListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=DeviceHistory.objects.all()
    serializer_class=DeviceHistorySerializer
    filter_class = DeviceHistoryFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class DeviceHistoryUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=DeviceHistory.objects.all()
    serializer_class=DeviceHistorySerializer
    # permission_classes=[IsAuthenticated]