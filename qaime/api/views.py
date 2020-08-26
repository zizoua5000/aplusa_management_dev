from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from qaime.api.serializers import QaimeSerializer
from qaime.api.models import Qaime
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from qaime.api.filters import QaimeFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class QaimeListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Qaime.objects.all()
    serializer_class=QaimeSerializer
    filter_class = QaimeFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class QaimeUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Qaime.objects.all()
    serializer_class=QaimeSerializer
    # permission_classes=[IsAuthenticated]