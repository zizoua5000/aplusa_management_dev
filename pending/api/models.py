from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from device.api.models import Device
from accessory.api.models import Accessory
from person.api.models import Person
from project.api.models import Project
from company.api.models import Company
from status.api.models import Status

class Pending(models.Model):
    device = models.ForeignKey(Device, models.DO_NOTHING, blank=False, null=False)
    accessory = models.ForeignKey(Accessory, models.DO_NOTHING, blank=False, null=False)
    count = models.BigIntegerField(default=0, blank=True, null=True)
    recipient = models.ForeignKey(Person, models.DO_NOTHING, blank=False, null=False)
    project = models.ForeignKey(Project, models.DO_NOTHING, blank=False, null=False)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=False, null=False)
    status = models.ForeignKey(Status, models.DO_NOTHING, blank=False, null=False)
    created_at = models.DateTimeField(editable=False)
    

    class Meta:
        managed = False
        db_table = 'pending'

    def save(self, *args,**kwargs):
        if not self.id:
            self.created_at=timezone.now()
        self.updated_at=timezone.now()
        return super(Pending, self).save( *args,**kwargs)

    def __str__(self):
        return self.project

