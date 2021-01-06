from rest_framework.serializers import ModelSerializer,SerializerMethodField
from accessory_history.api.models import AccessoryHistory
from rest_framework import serializers
from qaime.api.serializers import QaimeSerializer
from status.api.serializers import StatusSerializer


class AccessoryHistorySerializer(ModelSerializer):
        # entry_warehouse_date = serializers.DateTimeField(format=None,input_formats=None)
        status_detail=SerializerMethodField()
        qaime_detail=SerializerMethodField()
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
                'qaime_detail',
                'created_at',
                ]
        def get_qaime_detail(self,obj):
            return QaimeSerializer(obj.qaime).data
        def get_status_detail(self,obj):
            return StatusSerializer(obj.status).data
