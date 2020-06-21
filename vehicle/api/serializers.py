from rest_framework.serializers import ModelSerializer,SerializerMethodField
from vehicle.api.models import Vehicle
from vehicle_model.api.serializers import VehicleModelSerializer
from vehicle_type.api.serializers import VehicleTypeSerializer

class VehicleSerializer(ModelSerializer):
        vehicle_model_detail=SerializerMethodField()
        vehicle_type_detail=SerializerMethodField()
        class Meta:
            model=Vehicle
            fields=[
                'id',
                'plate',
                'serie_number',
                'comment',
                'vehicle_model',
                'vehicle_model_detail',
                'vehicle_type',
                'vehicle_type_detail',
                'created_at',
                'updated_at',
                ]

        def get_vehicle_model_detail(self,obj):
            return VehicleModelSerializer(obj.vehicle_model).data           
        def get_vehicle_type_detail(self,obj):
            return VehicleTypeSerializer(obj.vehicle_type).data

            

