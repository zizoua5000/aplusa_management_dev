from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from event.api.models import Event
from accessory.api.models import Accessory
from person.api.models import Person

class MEventAccessory(models.Model):
    event = models.ForeignKey(Event, models.DO_NOTHING, blank=False, null=False)
    accessory = models.ForeignKey(Accessory, models.DO_NOTHING, blank=False, null=False)
    count = models.BigIntegerField(default=0, blank=True, null=True)
    sell_price = models.FloatField(blank=False, null=False)
    recipient = models.ForeignKey(Person, models.DO_NOTHING,  blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_event_accessory'

    def save(self, *args,**kwargs):
        if not self.id:
            self.created_at=timezone.now()
        self.updated_at=timezone.now()
        return super(MEventAccessory, self).save( *args,**kwargs)

    def __str__(self):
        return self.event

