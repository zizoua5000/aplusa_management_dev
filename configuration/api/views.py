from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from configuration.api.serializers import ConfigurationSerializer
from configuration.api.models import Configuration
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from configuration.api.filters import ConfigurationFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class ConfigurationListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Configuration.objects.all()
    serializer_class=ConfigurationSerializer
    filter_class = ConfigurationFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class ConfigurationUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Configuration.objects.all()
    serializer_class=ConfigurationSerializer
    # permission_classes=[IsAuthenticated]