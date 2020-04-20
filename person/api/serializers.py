from rest_framework.serializers import ModelSerializer,SerializerMethodField
from person.api.models import Person
from company.api.serializers import CompanySerializer
from department.api.serializers import DepartmentSerializer
from job_title.api.serializers import JobTitleSerializer
from django.contrib.auth.models import User

class PersonSerializer(ModelSerializer):
        company_detail=SerializerMethodField()
        department_detail=SerializerMethodField()
        job_title_detail=SerializerMethodField()

        class Meta:
            model=Person
            fields=[
                'id',
                'first_name',
                'last_name',
                'phone',
                'email',
                'photo',
                'user',
                'company',
                'company_detail',
                'department',
                'department_detail',
                'job_title',
                'job_title_detail'
                ]

        def get_company_detail(self,obj):
            return CompanySerializer(obj.company).data
        def get_department_detail(self,obj):
            return DepartmentSerializer(obj.department).data
        def get_job_title_detail(self,obj):
            return JobTitleSerializer(obj.job_title).data

