from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from accessory.api.serializers import AccessorySerializer
from accessory.api.models import Accessory
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class AccessoryListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Accessory.objects.all()
    serializer_class=AccessorySerializer
    # permission_classes=[IsAuthenticated]

class AccessoryUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Accessory.objects.all()
    serializer_class=AccessorySerializer
    # permission_classes=[IsAuthenticated]