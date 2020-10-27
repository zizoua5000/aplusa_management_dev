from rest_framework.serializers import ModelSerializer,SerializerMethodField
from accessory_history.api.models import AccessoryHistory
from rest_framework import serializers


class AccessoryHistorySerializer(ModelSerializer):
        # entry_warehouse_date = serializers.DateTimeField(format=None,input_formats=None)
        class Meta:
            model=AccessoryHistory
            fields=[
                'id',
                'add_count',
                'rated_price',
                'entry_warehouse_date',
                'created_at',
                ]
