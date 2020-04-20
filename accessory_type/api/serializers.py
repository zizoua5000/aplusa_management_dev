from rest_framework.serializers import ModelSerializer
from accessory_type.api.models import AccessoryType

class AccessoryTypeSerializer(ModelSerializer):
        class Meta:
            model=AccessoryType
            fields=['id','name','created_at','updated_at']