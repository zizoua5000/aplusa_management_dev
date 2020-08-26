from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from event_type.api.serializers import EventTypeSerializer
from event_type.api.models import EventType
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from event_type.api.filters import EventTypeFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class EventTypeListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=EventType.objects.all()
    serializer_class=EventTypeSerializer
    filter_backends = (filter.DjangoFilterBackend,filters.OrderingFilter)
    filter_class = EventTypeFilter
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class EventTypeUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=EventType.objects.all()
    serializer_class=EventTypeSerializer
    # permission_classes=[IsAuthenticated]