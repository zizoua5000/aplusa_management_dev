from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from vehicle_model.api.serializers import VehicleModelSerializer
from vehicle.api.models import Vehicle
from vehicle_model.api.models import VehicleModel
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from vehicle_model.api.filters import VehicleModelFilter
from rest_framework import filters
from django_filters import rest_framework as filter


class VehicleModelListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=VehicleModel.objects.all().order_by('id')
    serializer_class=VehicleModelSerializer
    filter_class = VehicleModelFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    

class VehicleModelUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=VehicleModel.objects.all().order_by('id')
    serializer_class=VehicleModelSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if Vehicle.objects.filter(vehicle_model=instance.id).first():
            return Response("This is using in another table", status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
        return Response("Deleted", status=status.HTTP_200_OK)
        