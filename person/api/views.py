from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from person.api.serializers import PersonSerializer
from person.api.models import Person
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class PersonListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    # permission_classes=[IsAuthenticated]

class PersonUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    # permission_classes=[IsAuthenticated]