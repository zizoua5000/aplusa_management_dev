from rest_framework.serializers import ModelSerializer
from vehicle_type.api.models import VehicleType

class VehicleTypeSerializer(ModelSerializer):
        class Meta:
            model=VehicleType
            fields=['id','name','created_at','updated_at']



