from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from price.api.serializers import PriceSerializer
from price.api.models import Price
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class PriceListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Price.objects.all()
    serializer_class=PriceSerializer
    # permission_classes=[IsAuthenticated]

class PriceUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Price.objects.all()
    serializer_class=PriceSerializer
    # permission_classes=[IsAuthenticated]