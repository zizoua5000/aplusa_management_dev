from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from vehicle_mark.api.models import VehicleMark

class VehicleModel(models.Model):
    name = models.CharField(unique=True,max_length=50, blank=False, null=False)
    vehicle_mark = models.ForeignKey(VehicleMark, models.DO_NOTHING, blank=False, null=False)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    deleted_at = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'vehicle_model'

    def save(self, *args,**kwargs):
        if not self.id:
            self.created_at=timezone.now()
        self.updated_at=timezone.now()
        return super(VehicleModel, self).save( *args,**kwargs)

    def __str__(self):
        return self.name

