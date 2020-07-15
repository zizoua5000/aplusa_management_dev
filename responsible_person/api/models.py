from django.utils import timezone
from django.db import models
from department.api.models import Department
from person.api.models import Person

class ResponsiblePerson(models.Model):
    department = models.ForeignKey(Department, models.DO_NOTHING, blank=False, null=False)
    department_chief = models.ForeignKey(Person, models.DO_NOTHING, related_name='department_chief', blank=False, null=False)
    chief_substitute = models.ForeignKey(Person, models.DO_NOTHING, related_name='chief_substitute', blank=False, null=False)
    accounter = models.ForeignKey(Person, models.DO_NOTHING, related_name='accounter', blank=False, null=False)
    recipient = models.ForeignKey(Person, models.DO_NOTHING, related_name='recipient', blank=False, null=False)
    provider = models.ForeignKey(Person, models.DO_NOTHING, related_name='provider', blank=False, null=False)
    active = models.BooleanField(blank=False, null=False)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    deleted_at = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'responsible_person'

    def save(self, *args,**kwargs):
        if not self.id:
            self.created_at=timezone.now()
        self.updated_at=timezone.now()
        return super(ResponsiblePerson, self).save( *args,**kwargs)

    def __str__(self):
        return self.department_chief