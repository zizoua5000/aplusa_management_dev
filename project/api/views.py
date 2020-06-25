from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from project.api.serializers import ProjectSerializer
from project.api.models import Project
from project.api.filters import ProjectFilter
from rest_framework import filters
from django_filters import rest_framework as filter
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)



class ProjectListCreateAPIView(ListCreateAPIView):  
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Project.objects.all().order_by('id')
    serializer_class=ProjectSerializer
    filter_backends = (filter.DjangoFilterBackend,filters.OrderingFilter)
    filter_class = ProjectFilter
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class ProjectUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    # permission_classes=[IsAuthenticated]