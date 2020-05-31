from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from vehicle.api.serializers import VehicleSerializer
from vehicle.api.models import Vehicle
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from vehicle.api.filters import VehicleFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class VehicleListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Vehicle.objects.all()
    serializer_class=VehicleSerializer
    filter_class = VehicleFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class VehicleUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Vehicle.objects.all()
    serializer_class=VehicleSerializer
    # permission_classes=[IsAuthenticated]