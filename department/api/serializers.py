from rest_framework.serializers import ModelSerializer
from department.api.models import Department

class DepartmentSerializer(ModelSerializer):
        class Meta:
            model=Department
            fields=['id','name','created_at','updated_at']



