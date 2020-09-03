from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from event.api.serializers import EventSerializer
from event.api.models import Event
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from event.api.filters import EventFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class EventListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    filter_backends = (filter.DjangoFilterBackend,filters.OrderingFilter)
    filter_class = EventFilter
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class EventUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    # permission_classes=[IsAuthenticated]