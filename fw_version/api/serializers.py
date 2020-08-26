from rest_framework.serializers import ModelSerializer
from fw_version.api.models import FWVersion

class FWVersionSerializer(ModelSerializer):
        class Meta:
            model=FWVersion
            fields=['id','name','created_at','updated_at']



