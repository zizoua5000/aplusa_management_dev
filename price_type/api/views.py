from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from price_type.api.serializers import PriceTypeSerializer
from price_type.api.models import PriceType
from price_type.api.filters import PriceTypeFilter
from rest_framework import filters
from django_filters import rest_framework as filter
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)



class PriceTypeListCreateAPIView(ListCreateAPIView):  
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=PriceType.objects.all().order_by('id')
    serializer_class=PriceTypeSerializer
    filter_backends = (filter.DjangoFilterBackend,filters.OrderingFilter)
    filter_class = PriceTypeFilter
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class PriceTypeUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=PriceType.objects.all()
    serializer_class=PriceTypeSerializer
    # permission_classes=[IsAuthenticated]