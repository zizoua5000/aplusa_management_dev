from rest_framework.serializers import ModelSerializer
from region.api.models import Region

class RegionSerializer(ModelSerializer):
        class Meta:
            model=Region
            fields=['id','name','created_at','updated_at']



