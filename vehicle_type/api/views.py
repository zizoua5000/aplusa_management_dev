from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from vehicle_type.api.serializers import VehicleTypeSerializer
from vehicle_type.api.models import VehicleType
from vehicle_type.api.filters import VehicleTypeFilter
from rest_framework import filters
from django_filters import rest_framework as filter
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)



class VehicleTypeListCreateAPIView(ListCreateAPIView):  
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=VehicleType.objects.all().order_by('id')
    serializer_class=VehicleTypeSerializer
    filter_backends = (filter.DjangoFilterBackend,filters.OrderingFilter)
    filter_class = VehicleTypeFilter
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class VehicleTypeUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=VehicleType.objects.all()
    serializer_class=VehicleTypeSerializer
    # permission_classes=[IsAuthenticated]