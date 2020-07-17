from rest_framework.serializers import ModelSerializer,SerializerMethodField
from department.api.serializers import DepartmentSerializer
from person.api.serializers import PersonSerializer
from responsible_person.api.models import ResponsiblePerson

class ResponsiblePersonSerializer(ModelSerializer):
        department_detail=SerializerMethodField()
        department_chief_detail=SerializerMethodField()
        chief_substitute_detail=SerializerMethodField()
        accounter_detail=SerializerMethodField()
        recipient_detail=SerializerMethodField()
        provider_detail=SerializerMethodField()
        class Meta:
            model=ResponsiblePerson
            fields=[
                'id',
                'department',
                'department_detail',
                'department_chief',
                'department_chief_detail',
                'chief_substitute',
                'chief_substitute_detail',
                'accounter',
                'accounter_detail',
                'recipient',
                'recipient_detail',
                'provider',
                'provider_detail',
                'active',
                'created_at',
                'updated_at',
                ]

        def get_department_detail(self,obj):
            return DepartmentSerializer(obj.department).data 
        def get_department_chief_detail(self,obj):
            # print("OBJECT: ",str(obj))
            return PersonSerializer(obj.department_chief).data
        def get_chief_substitute_detail(self,obj):
            return PersonSerializer(obj.chief_substitute).data                       
        def get_accounter_detail(self,obj):
            return PersonSerializer(obj.accounter).data       
        def get_recipient_detail(self,obj):
            return PersonSerializer(obj.recipient).data
        def get_provider_detail(self,obj):
            return PersonSerializer(obj.provider).data            

