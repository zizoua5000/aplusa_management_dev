from rest_framework.serializers import ModelSerializer,SerializerMethodField
from device.api.models import Device
from device_detail.api.models import DeviceDetail
from company.api.serializers import CompanySerializer
from device_detail.api.serializers import DeviceDetailSerializer
from device_model.api.serializers import DeviceModelSerializer
from device_type.api.serializers import DeviceTypeSerializer

class DeviceSerializer(ModelSerializer):
        device_details = DeviceDetailSerializer(many=False)
        company_detail=SerializerMethodField()
        device_model_detail=SerializerMethodField()
        device_type_detail=SerializerMethodField()
        class Meta:
            model=Device
            fields=[
                'id',
                'serie',
                'company',
                'company_detail',
                'device_model',
                'device_model_detail',
                'device_type',
                'device_type_detail',
                'device_details',
                'created_at',
                'updated_at'
                ]

        def get_company_detail(self,obj):
            return CompanySerializer(obj.company).data
        def get_device_model_detail(self,obj):
            return DeviceModelSerializer(obj.device_model).data
        def get_device_type_detail(self,obj):
            return DeviceTypeSerializer(obj.device_type).data

        def create(self, validated_data):
            print("INITIAL VALIDATED DATA: ",validated_data)
            device_details_data = validated_data.pop('device_details')
            device = Device.objects.create(**validated_data)
            print("POPPED DATA ",device_details_data)
            DeviceDetail.objects.create(device=device,**device_details_data)           
            return device

        def update(self, instance, validated_data):
            print("UPDATE CALLED",validated_data)
            print("INSTANCE",instance)
            device_details_data = validated_data.pop('device_details')

            instance.serie = validated_data.get('serie', instance.serie)
            instance.company = validated_data.get('company', instance.company)
            instance.device_model = validated_data.get('device_model', instance.device_model)
            instance.device_type = validated_data.get('device_type', instance.device_type)
            instance.save()

            device_details = instance.device_details
            device_details.status=device_details_data.get('status',device_details.status)
            device_details.simcard=device_details_data.get('simcard',device_details.simcard)
            device_details.vehicle=device_details_data.get('vehicle',device_details.vehicle)
            device_details.company=device_details_data.get('company',device_details.company)
            device_details.device_location=device_details_data.get('device_location',device_details.device_location)
            device_details.configuration=device_details_data.get('configuration',device_details.configuration)
            device_details.fw_version=device_details_data.get('fw_version',device_details.fw_version)
            device_details.project=device_details_data.get('project',device_details.project)
            device_details.recipient=device_details_data.get('recipient',device_details.recipient)
            device_details.region=device_details_data.get('region',device_details.region)
            device_details.comment=device_details_data.get('comment',device_details.comment)
            device_details.price_datetime=device_details_data.get('price_datetime',device_details.price_datetime)
            device_details.status_datetime=device_details_data.get('status_datetime',device_details.status_datetime)
            device_details.sell_count=device_details_data.get('sell_count',device_details.sell_count)
            device_details.save()
            print(device_details)
            return instance
