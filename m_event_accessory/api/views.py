from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from m_event_accessory.api.serializers import MEventAccessorySerializer
from m_event_accessory.api.models import MEventAccessory
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from m_event_accessory.api.filters import MEventAccessoryFilter
from rest_framework import filters
from django_filters import rest_framework as filter

# from aplusa_management.filters import MVehicleAccessoryFilter
# from rest_framework import filters
# import django_filters


class MEventAccessoryListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=MEventAccessory.objects.all().order_by('id')
    serializer_class=MEventAccessorySerializer
    filter_class = MEventAccessoryFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    

class MEventAccessoryUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=MEventAccessory.objects.all().order_by('id')
    serializer_class=MEventAccessorySerializer
   
    
