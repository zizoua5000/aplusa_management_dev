from rest_framework.serializers import ModelSerializer,SerializerMethodField
from currency_rate.api.models import CurrencyRate


class CurrencyRateSerializer(ModelSerializer):
        class Meta:
            model=CurrencyRate
            fields=['id','start_date','end_date','rate','created_at']       

