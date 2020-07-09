from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveDestroyAPIView
# from user_permission.api.serializers import UserPermissionListSerializer,UserPermissionCreateSerializer,UserPermissionDeleteSerializer
from user_permission.api.serializers import UserPermissionListSerializer,UserPermissionCreateSerializer
from django.contrib.auth.models import User
from user_permission.api.models import UserPermission
from django.shortcuts import get_object_or_404
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from user_permission.api.filters import UserPermissionFilter
from rest_framework import filters
from django_filters import rest_framework as filter

# class MultipleFieldLookupMixin(object):
#     """
#     Apply this mixin to any view or viewset to get multiple field filtering
#     based on a `lookup_fields` attribute, instead of the default single field filtering.
#     """
#     def get_object(self):
#         queryset = self.get_queryset()             # Get the base queryset
#         queryset = self.filter_queryset(queryset)  # Apply any filter backends
#         filter = {}
#         for field in self.lookup_fields:
#             if self.kwargs[field]: # Ignore empty fields.
#                 filter[field] = self.kwargs[field]
#         obj = get_object_or_404(queryset, **filter)  # Lookup the object
#         self.check_object_permissions(self.request, obj)
#         return obj

class UserPermissionListAPIView(ListAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=User.objects.all()
    serializer_class=UserPermissionListSerializer
    filter_class = UserPermissionFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class UserPermissionDetailAPIView(RetrieveAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=User.objects.all()
    serializer_class=UserPermissionListSerializer
    # permission_classes=[IsAuthenticated]

class UserPermissionCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=UserPermission.objects.all()
    serializer_class=UserPermissionCreateSerializer
    # permission_classes=[IsAuthenticated]

# class UserPermissionDeleteAPIView(MultipleFieldLookupMixin,RetrieveDestroyAPIView):
#     permission_classes = (CustomDjangoModelPermissions, )
#     queryset=UserPermission.objects.all()
#     serializer_class=UserPermissionDeleteSerializer
#     lookup_fields = ('user', 'permission')
#     # permission_classes=[IsAuthenticated]


