from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from job_title.api.serializers import JobTitleSerializer
from job_title.api.models import JobTitle
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

class JobTitleListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=JobTitle.objects.all()
    serializer_class=JobTitleSerializer
    # permission_classes=[IsAuthenticated]

class JobTitleUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=JobTitle.objects.all()
    serializer_class=JobTitleSerializer
    # permission_classes=[IsAuthenticated]