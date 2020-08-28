from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from m_vehicle_accessory.api.serializers import MVehicleAccessorySerializer
from m_vehicle_accessory.api.models import MVehicleAccessory
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from m_vehicle_accessory.api.filters import MVehicleAccessoryFilter
from rest_framework import filters
from django_filters import rest_framework as filter

# from aplusa_management.filters import MVehicleAccessoryFilter
# from rest_framework import filters
# import django_filters


class MVehicleAccessoryListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=MVehicleAccessory.objects.all().order_by('id')
    serializer_class=MVehicleAccessorySerializer
    filter_class = MVehicleAccessoryFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    

class MVehicleAccessoryUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=MVehicleAccessory.objects.all().order_by('id')
    serializer_class=MVehicleAccessorySerializer
   
    
