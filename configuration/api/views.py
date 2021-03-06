from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from configuration.api.serializers import ConfigurationSerializer
from configuration.api.models import Configuration
from device_detail.api.models import DeviceDetail
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if DeviceDetail.objects.filter(fw_version=instance.id).first():
            return Response("This is using in another table", status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
        return Response("Deleted", status=status.HTTP_200_OK)