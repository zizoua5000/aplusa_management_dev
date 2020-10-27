from rest_framework.serializers import ModelSerializer,SerializerMethodField
from responsible_person.api.serializers import ResponsiblePersonSerializer
from person.api.serializers import PersonSerializer
from status.api.serializers import StatusSerializer
from qaime.api.models import Qaime

class QaimeSerializer(ModelSerializer): 
        responsible_person_detail=SerializerMethodField()
        recipient_detail=SerializerMethodField()
        class Meta:
            model=Qaime
            fields=[
                'id',
                'name',
                'responsible_person',
                'responsible_person_detail',
                'recipient',
                'recipient_detail',
                'qaime_type',
                'is_formal',
                'qaime_datetime',
                'comment',
                'created_at',
                'updated_at',
                ]
        def get_responsible_person_detail(self,obj):
            return ResponsiblePersonSerializer(obj.responsible_person).data 
        def get_recipient_detail(self,obj):
            return PersonSerializer(obj.recipient).data 


