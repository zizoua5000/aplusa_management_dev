from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from company_type.api.serializers import CompanyTypeSerializer
from company.api.models import Company
from company_type.api.models import CompanyType
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from company_type.api.filters import CompanyTypeFilter
from rest_framework import filters
from django_filters import rest_framework as filter


class CompanyTypeListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=CompanyType.objects.all().order_by('id')
    serializer_class=CompanyTypeSerializer
    filter_class = CompanyTypeFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class CompanyTypeUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=CompanyType.objects.all().order_by('id')
    serializer_class=CompanyTypeSerializer
    # permission_classes=[IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if Company.objects.filter(compaany_type=instance.id).first():
            return Response("This is using in another table", status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
        return Response("Deleted", status=status.HTTP_200_OK)