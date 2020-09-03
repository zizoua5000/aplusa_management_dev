from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from company.api.models import Company
from accessory.api.models import Accessory


class AccessoryHistory(models.Model):
    accessory = models.ForeignKey(Accessory, models.DO_NOTHING, blank=True, null=True)
    manufacturer = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    rated_price = models.FloatField(blank=False, null=False)
    count = models.BigIntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    deleted_at = models.DateTimeField(editable=False)

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
