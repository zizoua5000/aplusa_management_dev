from rest_framework.serializers import ModelSerializer
from action.api.models import Action

class ActionSerializer(ModelSerializer):
        class Meta:
            model=Action
            fields=['id','name','created_at','updated_at']



