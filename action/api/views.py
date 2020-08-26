from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from action.api.serializers import ActionSerializer
from action.api.models import Action
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from action.api.filters import ActionFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class ActionListCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Action.objects.all()
    serializer_class=ActionSerializer
    filter_backends = (filter.DjangoFilterBackend,filters.OrderingFilter)
    filter_class = ActionFilter
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class ActionUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Action.objects.all()
    serializer_class=ActionSerializer
    # permission_classes=[IsAuthenticated]