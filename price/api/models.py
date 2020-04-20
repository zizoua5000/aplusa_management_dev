from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from device_model.api.models import DeviceModel
from accessory_model.api.models import AccessoryModel
from price_type.api.models import PriceType
from project.api.models import Project

class Price(models.Model):
    start_datetime = models.DateTimeField(blank=False, null=False)
    end_datetime = models.DateTimeField(blank=True, null=True)
    price_type = models.ForeignKey(PriceType, models.DO_NOTHING, blank=False, null=False)
    sell_price = models.FloatField(blank=False, null=False)
    project = models.ForeignKey(Project, models.DO_NOTHING, blank=True, null=True)
    device_model = models.ForeignKey(DeviceModel, models.DO_NOTHING, blank=True, null=True)
    accessory_model = models.ForeignKey(AccessoryModel, models.DO_NOTHING, blank=True, null=True)
    # service_type_id = models.BigIntegerField(blank=True, null=True)
    is_second_hand = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'price'

    def save(self, *args,**kwargs):
        if not self.id:
            self.created_at=timezone.now()
        self.updated_at=timezone.now()
        return super(Price, self).save( *args,**kwargs)

    def __str__(self):
        return self.plate
