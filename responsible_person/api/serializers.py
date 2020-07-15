from rest_framework.serializers import ModelSerializer,SerializerMethodField
from department.api.serializers import DepartmentSerializer

class ResponsiblePersonSerializer(ModelSerializer):
        department_detail=SerializerMethodField()
        class Meta:
            model=ResponsiblePerson
            fields=[
                'id',
                'department',
                'department_detail',
                'department_chief',
                'chief_substitute',
                'accounter',
                'recipient',
                'active',
                'created_at',
                'updated_at',
                ]

        def get_department_detail(self,obj):
            return DepartmentSerializer(obj.department).data           
       

            

