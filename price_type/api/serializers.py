from rest_framework.serializers import ModelSerializer
from price_type.api.models import PriceType

class PriceTypeSerializer(ModelSerializer):
        class Meta:
            model=PriceType
            fields=['id','name','created_at','updated_at']



