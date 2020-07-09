from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from device_detail_view.api.serializers import DeviceDetailViewSerializer
from device_detail_view.api.models import DeviceDetailView
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class DeviceDetailViewListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=DeviceDetailView.objects.all()
    serializer_class=DeviceDetailViewSerializer
    # permission_classes=[IsAuthenticated]

class DeviceDetailViewUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=DeviceDetailView.objects.all()
    serializer_class=DeviceDetailViewSerializer
    # permission_classes=[IsAuthenticated]