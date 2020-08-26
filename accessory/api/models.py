from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from company.api.models import Company
from accessory_model.api.models import AccessoryModel
from accessory_type.api.models import AccessoryType

class Accessory(models.Model):
    name = models.CharField(unique=True,max_length=50, blank=False, null=False)
    accessory_model = models.ForeignKey(AccessoryModel, models.DO_NOTHING, blank=True, null=True)
    accessory_type = models.ForeignKey(AccessoryType, models.DO_NOTHING, blank=True, null=True)
    is_new = models.BooleanField(default=True, blank=True, null=True)
    is_our = models.BooleanField(default=True, blank=False, null=False)
    count = models.BigIntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    deleted_at = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'accessory'

    def save(self, *args,**kwargs):
        if not self.id:
            self.created_at=timezone.now()
        self.updated_at=timezone.now()
        return super(Accessory, self).save( *args,**kwargs)

    def __str__(self):
        return self.name
