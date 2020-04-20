from rest_framework.serializers import ModelSerializer,SerializerMethodField
from company.api.models import Company
from company_type.api.serializers import CompanyTypeSerializer

class CompanySerializer(ModelSerializer):
        main_company_detail=SerializerMethodField()
        company_type_detail=SerializerMethodField()
        class Meta:
            model=Company
            fields=[
                'id',
                'name',
                'main_company',
                'main_company_detail',
                'company_type',
                'company_type_detail',
                'created_at',
                'updated_at'
                ]

        def get_main_company_detail(self,obj):
            return CompanySerializer(obj.main_company).data
        def get_company_type_detail(self,obj):
            return CompanyTypeSerializer(obj.company_type).data

