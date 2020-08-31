from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from vehicle.api.models import Vehicle
from accessory.api.models import Accessory

class MVehicleAccessory(models.Model):
    vehicle = models.ForeignKey(Vehicle, models.DO_NOTHING, blank=False, null=False)
    accessory = models.ForeignKey(Accessory, models.DO_NOTHING, blank=False, null=False)
    count = models.BigIntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'm_vehicle_accessory'

    def save(self, *args,**kwargs):
        if not self.id:
            self.created_at=timezone.now()
        self.updated_at=timezone.now()
        return super(MVehicleAccessory, self).save( *args,**kwargs)

    def __str__(self):
        return self.project

