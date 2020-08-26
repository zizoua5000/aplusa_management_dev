from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from action_group.api.serializers import ActionGroupSerializer
from action_group.api.models import ActionGroup
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from action_group.api.filters import ActionGroupFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class ActionGroupListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=ActionGroup.objects.all()
    serializer_class=ActionGroupSerializer
    filter_backends = (filter.DjangoFilterBackend,filters.OrderingFilter)
    filter_class = ActionGroupFilter
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class ActionGroupUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=ActionGroup.objects.all()
    serializer_class=ActionGroupSerializer
    # permission_classes=[IsAuthenticated]