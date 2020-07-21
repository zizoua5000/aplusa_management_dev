from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from fw_version.api.serializers import FWVersionSerializer
from fw_version.api.models import FWVersion
from device_detail.api.models import DeviceDetail
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from fw_version.api.filters import FWVersionFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class FWVersionListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=FWVersion.objects.all()
    serializer_class=FWVersionSerializer
    filter_class = FWVersionFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class FWVersionUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=FWVersion.objects.all()
    serializer_class=FWVersionSerializer
    # permission_classes=[IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if DeviceDetail.objects.filter(fw_version=instance.id).first():
            return Response("This is using in another table", status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
        return Response("Deleted", status=status.HTTP_200_OK)