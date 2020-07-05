from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from accessory_type.api.serializers import AccessoryTypeSerializer
from accessory_type.api.models import AccessoryType
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from accessory_type.api.filters import AccessoryTypeFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class AccessoryTypeListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=AccessoryType.objects.all()
    serializer_class=AccessoryTypeSerializer
    filter_backends = (filter.DjangoFilterBackend,filters.OrderingFilter)
    filter_class = AccessoryTypeFilter
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class AccessoryTypeUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=AccessoryType.objects.all()
    serializer_class=AccessoryTypeSerializer
    # permission_classes=[IsAuthenticated]