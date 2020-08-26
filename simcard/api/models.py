from django.contrib.auth.models import User
from device.api.models import Device
from django.utils import timezone
from django.db import models

class Simcard(models.Model):
    number = models.CharField(unique=True,max_length=20, blank=False, null=False)
    package = models.BigIntegerField(blank=True, null=True)
    has_rouming = models.BooleanField(blank=False, null=False)
    is_active = models.BooleanField(blank=False, null=False)
    device = models.ForeignKey(Device, models.DO_NOTHING, blank=False, null=False)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    deleted_at = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'simcard'

    def save(self, *args,**kwargs):
        if not self.id:
            self.created_at=timezone.now()
        self.updated_at=timezone.now()
        return super(Simcard, self).save( *args,**kwargs)

    def __str__(self):
        return self.number
