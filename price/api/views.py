from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from price.api.serializers import PriceSerializer
from price.api.models import Price
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from price.api.filters import PriceFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class PriceListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Price.objects.all()
    serializer_class=PriceSerializer
    filter_class = PriceFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class PriceUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Price.objects.all()
    serializer_class=PriceSerializer
    # permission_classes=[IsAuthenticated]