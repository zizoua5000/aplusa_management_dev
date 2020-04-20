from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from status.api.serializers import StatusSerializer
from status.api.models import Status
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class StatusListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Status.objects.all()
    serializer_class=StatusSerializer
    # permission_classes=[IsAuthenticated]

class StatusUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Status.objects.all()
    serializer_class=StatusSerializer
    # permission_classes=[IsAuthenticated]