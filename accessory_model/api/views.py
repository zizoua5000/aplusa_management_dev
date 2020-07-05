from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from accessory_model.api.serializers import AccessoryModelSerializer
from accessory_model.api.models import AccessoryModel
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from accessory_model.api.filters import AccessoryModelFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class AccessoryModelListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=AccessoryModel.objects.all()
    serializer_class=AccessoryModelSerializer
    filter_backends = (filter.DjangoFilterBackend,filters.OrderingFilter)
    filter_class = AccessoryModelFilter
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class AccessoryModelUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=AccessoryModel.objects.all()
    serializer_class=AccessoryModelSerializer
    # permission_classes=[IsAuthenticated]