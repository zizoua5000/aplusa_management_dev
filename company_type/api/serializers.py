from rest_framework.serializers import ModelSerializer
from company_type.api.models import CompanyType

class CompanyTypeSerializer(ModelSerializer):
        class Meta:
            model=CompanyType
            fields=['id','name','created_at','updated_at']



