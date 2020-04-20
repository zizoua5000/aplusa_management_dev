from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from configuration.api.serializers import ConfigurationSerializer
from configuration.api.models import Configuration
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class ConfigurationListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Configuration.objects.all()
    serializer_class=ConfigurationSerializer
    # permission_classes=[IsAuthenticated]

class ConfigurationUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Configuration.objects.all()
    serializer_class=ConfigurationSerializer
    # permission_classes=[IsAuthenticated]