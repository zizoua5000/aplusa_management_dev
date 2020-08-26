from rest_framework.serializers import ModelSerializer
from action_group.api.models import ActionGroup

class ActionGroupSerializer(ModelSerializer):
        class Meta:
            model=ActionGroup
            fields=['id','name','created_at','updated_at']



