from rest_framework.serializers import ModelSerializer
from project.api.models import Project

class ProjectSerializer(ModelSerializer):
        class Meta:
            model=Project
            fields=['id','name','created_at','updated_at']



