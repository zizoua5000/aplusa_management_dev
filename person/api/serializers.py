from rest_framework.serializers import ModelSerializer,SerializerMethodField
from person.api.models import Person
from company.api.serializers import CompanySerializer
from department.api.serializers import DepartmentSerializer
from job_title.api.serializers import JobTitleSerializer
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
        class Meta:
            model = User
            fields = ['id', 'username', 'password','is_active']


class PersonSerializer(ModelSerializer):
        company_detail=SerializerMethodField()
        department_detail=SerializerMethodField()
        job_title_detail=SerializerMethodField()
        user_detail=SerializerMethodField()
        full_name = SerializerMethodField()
        class Meta:
            model=Person
            fields=[
                'id',
                'first_name',
                'last_name',
                'full_name',
                'phone',
                'email',
                'photo',
                'user',
                'user_detail',
                'company',
                'company_detail',
                'department',
                'department_detail',
                'job_title',
                'job_title_detail'
                ]

        def get_user_detail(self,obj):
            return UserSerializer(obj.user).data
        def get_company_detail(self,obj):
            return CompanySerializer(obj.company).data
        def get_department_detail(self,obj):
            return DepartmentSerializer(obj.department).data
        def get_job_title_detail(self,obj):
            return JobTitleSerializer(obj.job_title).data
        def get_full_name(self, obj):
            return '{} {}'.format(obj.first_name, obj.last_name) 

