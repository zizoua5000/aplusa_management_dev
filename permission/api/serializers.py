from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from django.contrib.auth.models import Permission
from content_type.api.serializers import ContentTypeSerializer

class PermissionSerializer(ModelSerializer):
        content_type_detail=SerializerMethodField()
        class Meta:
            model=Permission
            fields=[
                'id',
                'name',
                'codename',
                'content_type',
                'content_type_detail',
                ]

        def get_content_type_detail(self,obj):
            return ContentTypeSerializer(obj.content_type).data