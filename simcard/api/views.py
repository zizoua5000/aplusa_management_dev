from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from simcard.api.serializers import SimcardSerializer
from simcard.api.models import Simcard
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class SimcardListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Simcard.objects.all()
    serializer_class=SimcardSerializer
    # permission_classes=[IsAuthenticated]

class SimcardUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Simcard.objects.all()
    serializer_class=SimcardSerializer
    # permission_classes=[IsAuthenticated]