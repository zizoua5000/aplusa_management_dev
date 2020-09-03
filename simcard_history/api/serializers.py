from rest_framework.serializers import ModelSerializer,SerializerMethodField
from simcard_history.api.models import SimcardHistory
from simcard.api.serializers import SimcardSerializer

class SimcardHistorySerializer(ModelSerializer):
        simcard_detail=SerializerMethodField()
        class Meta:
            model=SimcardHistory
            fields=['id','package','simcard','simcard_detail','has_rouming','is_active','created_at']


        def get_simcard_detail(self,obj):
            return SimcardSerializer(obj.simcard).data

