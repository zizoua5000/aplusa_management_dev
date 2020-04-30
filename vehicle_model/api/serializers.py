from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from vehicle_model.api.models import VehicleModel
from vehicle_mark.api.serializers import VehicleMarkSerializer

class VehicleModelSerializer(ModelSerializer):
        vehicle_mark_detail=SerializerMethodField()
        class Meta:
            model=VehicleModel
            fields=['id','name','vehicle_mark','vehicle_mark_detail','created_at','updated_at']

        def get_vehicle_mark_detail(self,obj):
            return VehicleMarkSerializer(obj.vehicle_mark).data
