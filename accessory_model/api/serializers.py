from rest_framework.serializers import ModelSerializer
from accessory_model.api.models import AccessoryModel

class AccessoryModelSerializer(ModelSerializer):
        class Meta:
            model=AccessoryModel
            fields=['id','name','created_at','updated_at']