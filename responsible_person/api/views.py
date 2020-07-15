from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from responsible_person.api.serializers import ResponsiblePersonSerializer
from responsible_person.api.models import ResponsiblePerson
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from responsible_person.api.filters import ResponsiblePersonFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class ResponsiblePersonListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=ResponsiblePerson.objects.all()
    serializer_class=ResponsiblePersonSerializer
    filter_class = ResponsiblePersonFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class ResponsiblePersonUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=ResponsiblePerson.objects.all()
    serializer_class=ResponsiblePersonSerializer
    # permission_classes=[IsAuthenticated]