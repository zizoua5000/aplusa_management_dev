from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from vehicle_model.api.serializers import VehicleModelSerializer
from vehicle_model.api.models import VehicleModel
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
# from aplusa_management.pagination import CustomPagination

class VehicleModelListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=VehicleModel.objects.all()
    serializer_class=VehicleModelSerializer
    
    # permission_classes=[IsAuthenticated]

class VehicleModelUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=VehicleModel.objects.all()
    serializer_class=VehicleModelSerializer
    # permission_classes=[IsAuthenticated]