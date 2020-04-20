from rest_framework.serializers import ModelSerializer
from vehicle_mark.api.models import VehicleMark

class VehicleMarkSerializer(ModelSerializer):
        class Meta:
            model=VehicleMark
            fields=['id','name','created_at','updated_at']



