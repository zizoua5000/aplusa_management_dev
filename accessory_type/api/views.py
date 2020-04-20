from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from accessory_type.api.serializers import AccessoryTypeSerializer
from accessory_type.api.models import AccessoryType
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class AccessoryTypeListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=AccessoryType.objects.all()
    serializer_class=AccessoryTypeSerializer
    # permission_classes=[IsAuthenticated]

class AccessoryTypeUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=AccessoryType.objects.all()
    serializer_class=AccessoryTypeSerializer
    # permission_classes=[IsAuthenticated]