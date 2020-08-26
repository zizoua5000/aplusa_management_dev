from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from accessory_fixing.api.serializers import AccessoryFixingSerializer
from accessory_fixing.api.models import AccessoryFixing
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from accessory_fixing.api.filters import AccessoryFixingFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class AccessoryFixingListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=AccessoryFixing.objects.all()
    serializer_class=AccessoryFixingSerializer
    filter_class = AccessoryFixingFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class AccessoryFixingUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=AccessoryFixing.objects.all()
    serializer_class=AccessoryFixingSerializer
    # permission_classes=[IsAuthenticated]