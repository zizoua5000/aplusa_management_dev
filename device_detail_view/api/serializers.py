from rest_framework.serializers import ModelSerializer,SerializerMethodField
from device_detail_view.api.models import DeviceDetailView
from device.api.models import Device
from device_detail.api.models import DeviceDetail
from company.api.serializers import CompanySerializer
from device_model.api.serializers import DeviceModelSerializer
from device_type.api.serializers import DeviceTypeSerializer
from status.api.serializers import StatusSerializer
from simcard.api.serializers import SimcardSerializer
from vehicle.api.serializers import VehicleSerializer
from person.api.serializers import PersonSerializer
from device_location.api.serializers import DeviceLocationSerializer
from configuration.api.serializers import ConfigurationSerializer
from project.api.serializers import ProjectSerializer
from region.api.serializers import RegionSerializer

class DeviceDetailViewSerializer(ModelSerializer):
        company_detail=SerializerMethodField()
        device_model_detail=SerializerMethodField()
        device_type_detail=SerializerMethodField()
        status_detail=SerializerMethodField()
        simcard_detail=SerializerMethodField()
        vehicle_detail=SerializerMethodField()
        device_location_detail=SerializerMethodField()
        configuration_detail=SerializerMethodField()
        project_detail=SerializerMethodField()
        region_detail=SerializerMethodField()
        class Meta:
            model=DeviceDetailView
            fields=[
                'id',
                'serie',
                'device_model',
                'device_model_detail',
                'device_type',
                'device_type_detail',
                'status',
                'status_detail',
                'simcard',
                'simcard_detail',
                'vehicle',
                'vehicle_detail',
                'company',
                'company_detail',
                # 'recipient',
                # 'recipient_detail',
                'device_location',
                'device_location_detail',
                'configuration',
                'configuration_detail',
                'project',
                'project_detail',
                'region',
                'region_detail',
                'comment',
                'price_datetime',
                'status_datetime',
                'sell_count'
                ]
        def get_device_model_detail(self,obj):
            return DeviceModelSerializer(obj.device_model).data
        def get_device_type_detail(self,obj):
            return DeviceTypeSerializer(obj.device_type).data   
        def get_status_detail(self,obj):
            return StatusSerializer(obj.status).data
        def get_simcard_detail(self,obj):
            return SimcardSerializer(obj.simcard).data
        def get_vehicle_detail(self,obj):
            return VehicleSerializer(obj.vehicle).data
        def get_company_detail(self,obj):
            return CompanySerializer(obj.company).data
        # def get_recipient_detail(self,obj):
        #     return PersonSerializer(obj.recipient).data
        def get_device_location_detail(self,obj):
            return DeviceLocationSerializer(obj.device_location).data
        def get_configuration_detail(self,obj):
            return ConfigurationSerializer(obj.configuration).data
        def get_project_detail(self,obj):
            return ProjectSerializer(obj.project).data
        def get_region_detail(self,obj):
            return RegionSerializer(obj.region).data

        def create(self, validated_data):
            print("++++++++++++++++++++++++")
            deviceDetailView = DeviceDetailView.objects.create(**validated_data)
            serie_data = validated_data.pop('serie')
            device_model_data = validated_data.pop('device_model')
            device_type_data = validated_data.pop('device_type')
            
            # device_model_detail_data = validated_data.pop('device_model_detail')
            print(serie_data)
            print(device_model_data)
            print(device_type_data)
            print("VALIDATE DATA: ",validated_data)
            deviceDetail = DeviceDetail.objects.create(**validated_data)
            dataX={'serie':serie_data,'device_model':device_model_data,'device_type':device_type_data,'device_detail':deviceDetail}
            device = Device.objects.create(**dataX)
            print("DEVICE DETAIL: ",deviceDetail)
            print("DEVICE : ",device)
            print("DEVICE VIew : ",deviceDetailView)
            print("++++++++++++++++++++++++")
            return deviceDetailView



