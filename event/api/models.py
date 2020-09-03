from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from action.api.models import Action
from event_type.api.models import EventType
from device_history.api.models import DeviceHistory
from accessory_history.api.models import AccessoryHistory
from accessory_fixing.api.models import AccessoryFixing
from simcard_history.api.models import SimcardHistory
from region.api.models import Region


class Event(models.Model):
    action = models.ForeignKey(Action, models.DO_NOTHING, blank=True, null=True)
    event_type = models.ForeignKey(EventType, models.DO_NOTHING, blank=True, null=True)
    device_history = models.ForeignKey(DeviceHistory, models.DO_NOTHING, blank=True, null=True)
    accessory_history = models.ForeignKey(AccessoryHistory, models.DO_NOTHING, blank=True, null=True)
    accessory_fixing = models.ForeignKey(AccessoryFixing, models.DO_NOTHING, blank=True, null=True)
    simcard_history = models.ForeignKey(SimcardHistory, models.DO_NOTHING, blank=True, null=True)
    event_region = models.ForeignKey(Region, models.DO_NOTHING, blank=True, null=True)
    event_datetime = models.DateTimeField(editable=False)
    event_price = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'event'

    def save(self, *args,**kwargs):
        if not self.id:
            self.created_at=timezone.now()
        self.updated_at=timezone.now()
        return super(Event, self).save( *args,**kwargs)

    def __str__(self):
        return self.action.name
