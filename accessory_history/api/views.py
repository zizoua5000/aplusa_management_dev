from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from accessory_history.api.serializers import AccessoryHistorySerializer
from accessory_history.api.models import AccessoryHistory
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from accessory_history.api.filters import AccessoryHistoryFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class AccessoryHistoryListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset = AccessoryHistory.objects.all().order_by('id')
    serializer_class=AccessoryHistorySerializer
    filter_class = AccessoryHistoryFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class AccessoryHistoryUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=AccessoryHistory.objects.all().order_by('id')
    serializer_class=AccessoryHistorySerializer
    # permission_classes=[IsAuthenticated]