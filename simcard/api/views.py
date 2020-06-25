from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from simcard.api.serializers import SimcardSerializer
from simcard.api.models import Simcard
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

from simcard.api.filters import SimcardFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class SimcardListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Simcard.objects.all().order_by('id')
    serializer_class=SimcardSerializer
    filter_class = SimcardFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class SimcardUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Simcard.objects.all()
    serializer_class=SimcardSerializer
    # permission_classes=[IsAuthenticated]
    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     if Simcard.objects.filter(simcard=instance.id).first():
    #         return Response("This is using in another table", status=status.HTTP_400_BAD_REQUEST)
    #     self.perform_destroy(instance)
    #     return Response("Deleted", status=status.HTTP_200_OK)    