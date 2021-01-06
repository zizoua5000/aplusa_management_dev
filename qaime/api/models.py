from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from responsible_person.api.models import ResponsiblePerson
from person.api.models import Person
from status.api.models import Status
from qaime_type.api.models import QaimeType

class Qaime(models.Model):
    name = models.CharField(unique=True,max_length=50, blank=False, null=False)
    responsible_person = models.ForeignKey(ResponsiblePerson, models.DO_NOTHING, blank=False, null=False)
    recipient = models.ForeignKey(Person, models.DO_NOTHING, blank=False, null=False)
    status = models.ForeignKey(Status, models.DO_NOTHING, blank=False, null=False)
    qaime_type = models.ForeignKey(QaimeType, models.DO_NOTHING, blank=False, null=False)
    is_formal = models.BooleanField(blank=False, null=False,default=True)
    qaime_datetime = models.DateTimeField(blank=False, null=False)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    deleted_at = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'qaime'

    def save(self, *args,**kwargs):
        if not self.id:
            self.created_at=timezone.now()
        self.updated_at=timezone.now()
        return super(Qaime, self).save( *args,**kwargs)

    def __str__(self):
        return self.name
        
