from rest_framework.serializers import ModelSerializer
from simcard.api.models import Simcard

class SimcardSerializer(ModelSerializer):
        class Meta:
            model=Simcard
            fields=['id','number','package','has_roumnig','is_active','created_at','updated_at']



