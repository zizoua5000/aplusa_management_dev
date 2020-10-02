from django.contrib.auth.models import User
# from device.api.models import Device
from simcard.api.models import Simcard
from django.utils import timezone
from django.db import models

class SimcardHistory(models.Model):
    simcard = models.ForeignKey(Simcard, models.DO_NOTHING, blank=False, null=False)
    package = models.BigIntegerField(blank=True, null=True)
    has_rouming = models.BooleanField(blank=False, null=False)
    is_active = models.BooleanField(blank=False, null=False)
    # device = models.ForeignKey(Device, models.DO_NOTHING, blank=False, null=False)
    created_at = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'simcard_history'

    def save(self, *args,**kwargs):
        if not self.id:
            self.created_at=timezone.now()
        self.updated_at=timezone.now()
        return super(SimcardHistory, self).save( *args,**kwargs)

    def __str__(self):
        return self.simcard.number
