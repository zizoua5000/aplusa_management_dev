from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from project.api.serializers import ProjectSerializer
from project.api.models import Project
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class ProjectListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    # permission_classes=[IsAuthenticated]

class ProjectUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    # permission_classes=[IsAuthenticated]