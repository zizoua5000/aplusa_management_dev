from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from company.api.models import Company
from accessory.api.models import Accessory
from vehicle.api.models import Vehicle
from status.api.models import Status


class AccessoryFixing(models.Model):
    accessory = models.ForeignKey(Accessory, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    vehicle = models.ForeignKey(Vehicle, models.DO_NOTHING, blank=True, null=True)
    accessory_status = models.ForeignKey(Status, models.DO_NOTHING, blank=True, null=True)
    accessory_event_datetime = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    deleted_at = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'accessory_fixing'

    def save(self, *args,**kwargs):
        if not self.id:
            self.created_at=timezone.now()
        self.updated_at=timezone.now()
        return super(AccessoryFixing, self).save( *args,**kwargs)

    def __str__(self):
        return self.accessory.name
