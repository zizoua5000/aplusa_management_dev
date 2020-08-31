from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from pending.api.serializers import PendingSerializer
from pending.api.models import Pending
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from pending.api.filters import PendingFilter
from rest_framework import filters
from django_filters import rest_framework as filter

# from aplusa_management.filters import MProjectCompanyFilter
# from rest_framework import filters
# import django_filters


class PendingListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Pending.objects.all().order_by('id')
    serializer_class=PendingSerializer
    filter_class = PendingFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    

class PendingUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Pending.objects.all().order_by('id')
    serializer_class=PendingSerializer
   
    
