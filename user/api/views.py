from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from user.api.serializers import UserRegisterSerializer,UserUpdateDeleteSerializer
from django.contrib.auth.models import User
from person.api.models import Person
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from user.api.filters import UserFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class UserRegisterListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=User.objects.all()
    serializer_class=UserRegisterSerializer
    filter_class = UserFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class UserUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=User.objects.all()
    serializer_class=UserUpdateDeleteSerializer
    # permission_classes=[IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if Person.objects.filter(user=instance.id).first():
            return Response("This is using in another table", status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
        return Response("Deleted", status=status.HTTP_200_OK)