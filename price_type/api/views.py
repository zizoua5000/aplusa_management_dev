from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from price_type.api.serializers import PriceTypeSerializer
from price_type.api.models import PriceType
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class PriceTypeListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=PriceType.objects.all()
    serializer_class=PriceTypeSerializer
    # permission_classes=[IsAuthenticated]

class PriceTypeUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=PriceType.objects.all()
    serializer_class=PriceTypeSerializer
    # permission_classes=[IsAuthenticated]