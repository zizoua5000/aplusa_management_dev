from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from event.api.models import Event
from person.api.models import Person

class MEventPerson(models.Model):
    event = models.ForeignKey(Event, models.DO_NOTHING, blank=False, null=False)
    person = models.ForeignKey(Person, models.DO_NOTHING, blank=False, null=False)
    class Meta:
        managed = False
        db_table = 'm_event_person'

    def save(self, *args,**kwargs):
        if not self.id:
            self.created_at=timezone.now()
        self.updated_at=timezone.now()
        return super(MEventPerson, self).save( *args,**kwargs)

    def __str__(self):
        return self.event

