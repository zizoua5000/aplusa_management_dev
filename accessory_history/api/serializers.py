from rest_framework.serializers import ModelSerializer,SerializerMethodField
from accessory_history.api.models import AccessoryHistory
from rest_framework import serializers
from status.api.serializers import StatusSerializer


class AccessoryHistorySerializer(ModelSerializer):
        # entry_warehouse_date = serializers.DateTimeField(format=None,input_formats=None)
        status_detail=SerializerMethodField()
        class Meta:
            model=AccessoryHistory
            fields=[
                'id',
                'add_count',
                'rated_price',
                'entry_warehouse_date',
                'status',
                'status_detail',
                'qaime',
                'created_at',
                ]
        def get_status_detail(self,obj):
            return StatusSerializer(obj.status).data

        def to_internal_value(self, data):
            if data.get('rated_price') == '':

                data['rated_price'] = None

            return super(AccessoryHistorySerializer, self).to_internal_value(data)
