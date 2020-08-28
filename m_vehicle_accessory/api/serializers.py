from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from m_vehicle_accessory.api.models import MVehicleAccessory
from vehicle.api.serializers import VehicleSerializer
from accessory.api.serializers import AccessorySerializer

class MVehicleAccessorySerializer(ModelSerializer):
        vehicle_detail=SerializerMethodField()
        accessory_detail=SerializerMethodField()
        class Meta:
            model=MVehicleAccessory
            fields=['id','vehicle','vehicle_detail','accessory','accessory_detail','count','created_at']

        def get_vehicle_detail(self,obj):
            return VehicleSerializer(obj.vehicle).data
        def get_accessory_detail(self,obj):
            return AccessorySerializer(obj.accessory).data
