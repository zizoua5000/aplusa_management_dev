from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from vehicle_mark.api.serializers import VehicleMarkSerializer
from vehicle_mark.api.models import VehicleMark
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from vehicle_mark.api.filters import VehicleMarkFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class VehicleMarkListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=VehicleMark.objects.all().order_by('id')
    serializer_class=VehicleMarkSerializer
    filter_class = VehicleMarkFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class VehicleMarkUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=VehicleMark.objects.all().order_by('id')
    serializer_class=VehicleMarkSerializer
    # permission_classes=[IsAuthenticated]