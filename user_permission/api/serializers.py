from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from rest_framework import status
from django.http import HttpResponse
from rest_framework.response import Response
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
        validators = []


# class UserPermissionCreateSerializer(ModelSerializer):
#     class Meta:
#         model = UserPermission
#         fields = '__all__'

class UserPermissionCreateSerializer(ModelSerializer):
    permissions = PermissionSerializer(many=True)
    class Meta: 
        model = UserPermission
        fields = ('user','permissions')
    
    def create(self, validated_data):
        user=validated_data.get('user')
        permissions=validated_data.get('permissions')

        # First of all delete old many to many relation data
        user_permission_old=UserPermission.objects.filter(user=user)
        if user_permission_old:
            for user_per in user_permission_old:
                user_per.delete()

        # After cretae new many to many relation data
        for permission in permissions:
            p=Permission.objects.filter(codename=permission['codename'],content_type=permission['content_type']).first()
            UserPermission.objects.create(user=user,permission=p)
        return user
    
    def to_representation(self, instance):
        serializer = UserPermissionListSerializer(instance)
        return serializer.data

# class UserPermissionDeleteSerializer(ModelSerializer):
#     class Meta:
#         model = UserPermission
#         fields = '__all__'



