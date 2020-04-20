from rest_framework.serializers import ModelSerializer
from job_title.api.models import JobTitle

class JobTitleSerializer(ModelSerializer):
        class Meta:
            model=JobTitle
            fields=['id','name','created_at','updated_at']



