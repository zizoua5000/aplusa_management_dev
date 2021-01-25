from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from accessory.api.models import Accessory
from qaime.api.models import Qaime
from status.api.models import Status

class AccessoryHistory(models.Model):
    accessory = models.ForeignKey(Accessory,related_name='accessory_histories',on_delete=models.CASCADE)
    add_count = models.BigIntegerField(blank=True, null=True)
    rated_price = models.FloatField(blank=True, null=True)
    entry_warehouse_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(editable=False)
    qaime = models.ForeignKey(Qaime, models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey(Status, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accessory_history'
        
    def save(self, *args,**kwargs):
        if not self.id:
            self.created_at=timezone.now()
        self.updated_at=timezone.now()
        return super(AccessoryHistory, self).save( *args,**kwargs)

    def __str__(self):
        return self.accessory.name
