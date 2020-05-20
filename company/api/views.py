from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from company.api.serializers import CompanySerializer
from company.api.models import Company
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from company.api.filters import CompanyFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class CompanyListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Company.objects.all().order_by('id')
    serializer_class=CompanySerializer
    filter_class = CompanyFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class CompanyUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Company.objects.all().order_by('id')
    serializer_class=CompanySerializer
    # permission_classes=[IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if Company.objects.filter(main_company=instance.id).first():
            return Response("This is using in another table", status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
        return Response("Deleted", status=status.HTTP_200_OK)