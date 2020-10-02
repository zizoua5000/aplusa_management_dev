from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from currency_rate.api.serializers import CurrencyRateSerializer
from currency_rate.api.models import CurrencyRate
from currency_rate.api.filters import CurrencyRateFilter
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

from rest_framework import filters
from django_filters import rest_framework as filter

class CurrencyRateListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=CurrencyRate.objects.all()
    serializer_class=CurrencyRateSerializer
    filter_backends = (filter.DjangoFilterBackend,filters.OrderingFilter)
    filter_class = CurrencyRateFilter
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class CurrencyRateUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=CurrencyRate.objects.all()
    serializer_class=CurrencyRateSerializer
    # permission_classes=[IsAuthenticated]