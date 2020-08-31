from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from m_project_company.api.models import MProjectCompany
from project.api.serializers import ProjectSerializer
from company.api.serializers import CompanySerializer

class MProjectCompanySerializer(ModelSerializer):
        project_detail=SerializerMethodField()
        company_detail=SerializerMethodField()
        class Meta:
            model=MProjectCompany
            fields=['id','project','project_detail','company','company_detail','created_at']

        def get_project_detail(self,obj):
            return ProjectSerializer(obj.project).data
        def get_company_detail(self,obj):
            return CompanySerializer(obj.company).data
