from rest_framework.serializers import ModelSerializer
from qaime_type.api.models import QaimeType

class QaimeTypeSerializer(ModelSerializer):
        class Meta:
            model=QaimeType
            fields=['id','name','created_at','updated_at']



