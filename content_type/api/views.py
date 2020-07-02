from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from content_type.api.serializers import ContentTypeSerializer
from django.contrib.auth.models import ContentType
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from content_type.api.filters import ContentTypeFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class ContentTypeListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=ContentType.objects.all()
    serializer_class=ContentTypeSerializer
    filter_backends = (filter.DjangoFilterBackend,filters.OrderingFilter)
    filter_class = ContentTypeFilter
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class ContentTypeUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=ContentType.objects.all()
    serializer_class=ContentTypeSerializer
    # permission_classes=[IsAuthenticated]