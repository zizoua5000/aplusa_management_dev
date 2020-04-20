from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

class UserRegisterSerializer(ModelSerializer):
        password=serializers.CharField(write_only=True) 
        class Meta:
            model=User
            fields=[
                'id',
                'username',
                'password',
                'is_active'
                ]

        def validate(self,attr):
           validate_password(attr['password'])
           return attr
        
        def create(self,validated_data):
            user=User.objects.create(
                username=validated_data["username"]
            )
            user.set_password(validated_data['password'])
            user.is_active=validated_data['is_active']
            user.save()
            return user


class UserUpdateDeleteSerializer(ModelSerializer):
        password=serializers.CharField(write_only=True, required=False, allow_blank=True)
        class Meta:
            model=User
            fields=[
                'id',
                'username',
                'password',
                'is_active'
                ]

        def validate(self,attr):
            if attr['password']:
                validate_password(attr['password'])
            return attr
        
        def update(self,instance,validated_data):
            instance.username=validated_data.get('username',instance.username)
            instance.is_active=validated_data.get('is_active',instance.is_active)

            if validated_data.get('password')!="":
                instance.set_password(validated_data['password'])
            else:
                instance.password=instance.password
            instance.save()
            return instance