from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from vehicle_model.api.models import VehicleModel
from vehicle_type.api.models import VehicleType

class Vehicle(models.Model):
    plate = models.CharField(unique=True,max_length=50, blank=False, null=False)
    serie_number = models.CharField(max_length=50, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    vehicle_model = models.ForeignKey(VehicleModel, models.DO_NOTHING, blank=False, null=False)
    vehicle_type = models.ForeignKey(VehicleType, models.DO_NOTHING, blank=False, null=False)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    deleted_at = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'vehicle'

    def save(self, *args,**kwargs):
        if not self.id:
            self.created_at=timezone.now()
        self.updated_at=timezone.now()
        return super(Vehicle, self).save( *args,**kwargs)

    def __str__(self):
        return self.plate
