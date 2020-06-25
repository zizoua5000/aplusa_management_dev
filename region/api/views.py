from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from region.api.serializers import RegionSerializer
from region.api.models import Region
from region.api.filters import RegionFilter
from rest_framework import filters
from django_filters import rest_framework as filter
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)



class RegionListCreateAPIView(ListCreateAPIView):  
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Region.objects.all().order_by('id')
    serializer_class=RegionSerializer
    filter_backends = (filter.DjangoFilterBackend,filters.OrderingFilter)
    filter_class = RegionFilter
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class RegionUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Region.objects.all()
    serializer_class=RegionSerializer
    # permission_classes=[IsAuthenticated]