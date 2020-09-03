from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from simcard_history.api.serializers import SimcardHistorySerializer
from simcard_history.api.models import SimcardHistory
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

from simcard_history.api.filters import SimcardHistoryFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class SimcardHistoryListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=SimcardHistory.objects.all().order_by('id')
    serializer_class=SimcardHistorySerializer
    filter_class = SimcardHistoryFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class SimcardHistoryUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=SimcardHistory.objects.all()
    serializer_class=SimcardHistorySerializer
    # permission_classes=[IsAuthenticated]
    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     if Simcard.objects.filter(simcard=instance.id).first():
    #         return Response("This is using in another table", status=status.HTTP_400_BAD_REQUEST)
    #     self.perform_destroy(instance)
    #     return Response("Deleted", status=status.HTTP_200_OK)    