from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from accessory.api.serializers import AccessorySerializer
from accessory.api.models import Accessory
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from accessory.api.filters import AccessoryFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class AccessoryListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset = Accessory.objects.all().order_by('id')
    serializer_class=AccessorySerializer
    filter_class = AccessoryFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class AccessoryUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Accessory.objects.all().order_by('id')
    serializer_class=AccessorySerializer
    # permission_classes=[IsAuthenticated]