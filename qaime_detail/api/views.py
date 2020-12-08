from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from qaime_detail.api.serializers import QaimeDetailListSerializer
from qaime_detail.api.models import QaimeDetail
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from qaime_detail.api.filters import QaimeDetailFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class QaimeDetailListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=QaimeDetail.objects.all()
    serializer_class=QaimeDetailListSerializer
    filter_class = QaimeDetailFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class QaimeDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=QaimeDetail.objects.all()
    serializer_class=QaimeDetailListSerializer
    # permission_classes=[IsAuthenticated]