from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from qaime_type.api.serializers import QaimeTypeSerializer
from qaime_type.api.models import QaimeType
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from qaime_type.api.filters import QaimeTypeFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class QaimeTypeListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=QaimeType.objects.all()
    serializer_class=QaimeTypeSerializer
    filter_backends = (filter.DjangoFilterBackend,filters.OrderingFilter)
    filter_class = QaimeTypeFilter
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class QaimeTypeUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=QaimeType.objects.all()
    serializer_class=QaimeTypeSerializer
    # permission_classes=[IsAuthenticated]