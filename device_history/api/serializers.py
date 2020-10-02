from rest_framework.serializers import ModelSerializer,SerializerMethodField
from device_history.api.models import DeviceHistory
from company.api.serializers import CompanySerializer
from device_detail.api.serializers import DeviceDetailSerializer
from device_model.api.serializers import DeviceModelSerializer
from device_type.api.serializers import DeviceTypeSerializer
from status.api.serializers import StatusSerializer
from simcard.api.serializers import SimcardSerializer
from vehicle.api.serializers import VehicleSerializer
from company.api.serializers import CompanySerializer
from person.api.serializers import PersonSerializer
from device_location.api.serializers import DeviceLocationSerializer
from configuration.api.serializers import ConfigurationSerializer
from project.api.serializers import ProjectSerializer
from fw_version.api.serializers import FWVersionSerializer

class DeviceHistorySerializer(ModelSerializer):
        # device_details = DeviceDetailSerializer(many=False)
        company_detail=SerializerMethodField()
        device_model_detail=SerializerMethodField()
        device_type_detail=SerializerMethodField()
        status_detail=SerializerMethodField()
        simcard_detail=SerializerMethodField()
        vehicle_detail=SerializerMethodField()
        manufacturer_detail=SerializerMethodField()
        recipient_detail=SerializerMethodField()
        device_location_detail=SerializerMethodField()
        configuration_detail=SerializerMethodField()
        project_detail=SerializerMethodField()
        fw_version_detail=SerializerMethodField()
        class Meta:
            model=DeviceHistory
            fields=[
                'id','serie','company','company_detail','device_model','device_model_detail',
                'device_type','device_type_detail','manufacturer','manufacturer_detail',
                'status','status_detail','simcard','simcard_detail','vehicle','vehicle_detail',
                'recipient','recipient_detail','device_location','device_location_detail',
                'configuration','configuration_detail','project','project_detail',
                'fw_version','fw_version_detail','sell_count','rated_price',
                'guarantee_to_us','guarantee_from_us','manufacture_date','buy_date',
                'entry_warehouse_date','webtrack_status','is_our','is_rent',
                'is_sold','sell_price','device_event_datetime','comment',
                'created_at',
                'updated_at'
                ]

        def get_company_detail(self,obj):
            return CompanySerializer(obj.company).data
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
        def get_manufacturer_detail(self,obj):
            return CompanySerializer(obj.manufacturer).data
        def get_recipient_detail(self,obj):
            return PersonSerializer(obj.recipient).data
        def get_device_location_detail(self,obj):
            return DeviceLocationSerializer(obj.device_location).data
        def get_configuration_detail(self,obj):
            return ConfigurationSerializer(obj.configuration).data
        def get_project_detail(self,obj):
            return ProjectSerializer(obj.project).data
        def get_fw_version_detail(self,obj):
            return FWVersionSerializer(obj.fw_version).data

        # def create(self, validated_data):
        #     print("INITIAL VALIDATED DATA: ",validated_data)
        #     device_details_data = validated_data.pop('device_details')
        #     device = Device.objects.create(**validated_data)
        #     print("POPPED DATA ",device_details_data)
        #     DeviceDetail.objects.create(device=device,**device_details_data)           
        #     return device

        # def update(self, instance, validated_data):
        #     print("UPDATE CALLED",validated_data)
        #     print("INSTANCE",instance)
        #     device_details_data = validated_data.pop('device_details')

        #     instance.serie = validated_data.get('serie', instance.serie)
        #     instance.company = validated_data.get('company', instance.company)
        #     instance.device_model = validated_data.get('device_model', instance.device_model)
        #     instance.device_type = validated_data.get('device_type', instance.device_type)
        #     instance.save()

        #     device_details = instance.device_details
        #     device_details.status=device_details_data.get('status',device_details.status)
        #     device_details.simcard=device_details_data.get('simcard',device_details.simcard)
        #     device_details.vehicle=device_details_data.get('vehicle',device_details.vehicle)
        #     device_details.company=device_details_data.get('company',device_details.company)
        #     device_details.device_location=device_details_data.get('device_location',device_details.device_location)
        #     device_details.configuration=device_details_data.get('configuration',device_details.configuration)
        #     device_details.fw_version=device_details_data.get('fw_version',device_details.fw_version)
        #     device_details.project=device_details_data.get('project',device_details.project)
        #     device_details.recipient=device_details_data.get('recipient',device_details.recipient)
        #     device_details.region=device_details_data.get('region',device_details.region)
        #     device_details.comment=device_details_data.get('comment',device_details.comment)
        #     device_details.price_datetime=device_details_data.get('price_datetime',device_details.price_datetime)
        #     device_details.status_datetime=device_details_data.get('status_datetime',device_details.status_datetime)
        #     device_details.sell_count=device_details_data.get('sell_count',device_details.sell_count)
        #     device_details.save()
        #     print(device_details)
        #     return instance
