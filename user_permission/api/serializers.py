from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from user_permission.api.models import UserPermission
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class UserPermissionListSerializer(ModelSerializer):
    user_permissions_detail=SerializerMethodField()
    class Meta:
        model = User
        fields = ('id', 'username','user_permissions_detail')

    def get_user_permissions_detail(self,obj):
        return PermissionSerializer(Permission.objects.filter(user=obj), many=True).data

class PermissionSerializer(ModelSerializer):  
    class Meta:
        model = Permission
        fields = '__all__'

class UserPermissionCreateSerializer(ModelSerializer):
    class Meta:
        model = UserPermission
        fields = '__all__'

class UserPermissionDeleteSerializer(ModelSerializer):
    class Meta:
        model = UserPermission
        fields = '__all__'

