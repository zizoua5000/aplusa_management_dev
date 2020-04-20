from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from region.api.serializers import RegionSerializer
from region.api.models import Region
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class RegionListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Region.objects.all()
    serializer_class=RegionSerializer
    # permission_classes=[IsAuthenticated]

class RegionUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Region.objects.all()
    serializer_class=RegionSerializer
    # permission_classes=[IsAuthenticated]