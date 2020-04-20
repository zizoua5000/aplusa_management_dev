from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from user.api.serializers import UserRegisterSerializer,UserUpdateDeleteSerializer
from django.contrib.auth.models import User
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class UserRegisterListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=User.objects.all()
    serializer_class=UserRegisterSerializer
    # permission_classes=[IsAuthenticated]

class UserUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=User.objects.all()
    serializer_class=UserUpdateDeleteSerializer
    # permission_classes=[IsAuthenticated]