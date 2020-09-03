from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from m_event_person.api.serializers import MEventPersonSerializer
from m_event_person.api.models import MEventPerson
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from m_event_person.api.filters import MEventPersonFilter
from rest_framework import filters
from django_filters import rest_framework as filter

# from aplusa_management.filters import MVehicleAccessoryFilter
# from rest_framework import filters
# import django_filters


class MEventPersonListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=MEventPerson.objects.all().order_by('id')
    serializer_class=MEventPersonSerializer
    filter_class = MEventPersonFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    

class MEventPersonUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=MEventPerson.objects.all().order_by('id')
    serializer_class=MEventPersonSerializer
   
    
