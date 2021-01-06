from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from qaime.api.models import Qaime
from device.api.models import Device
from accessory.api.models import Accessory
from simcard.api.models import Simcard
from project.api.models import Project
from company.api.models import Company
from configuration.api.models import Configuration
from fw_version.api.models import FWVersion

class QaimeDetail(models.Model):
    qaime = models.ForeignKey(Qaime, models.DO_NOTHING, blank=False, null=True)
    device = models.ForeignKey(Device, models.DO_NOTHING, blank=False, null=True)
    accessory = models.ForeignKey(Accessory, models.DO_NOTHING, blank=False, null=True)
    simcard = models.ForeignKey(Simcard, models.DO_NOTHING, blank=False, null=True)
    project = models.ForeignKey(Project, models.DO_NOTHING, blank=False, null=False)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=False, null=False)
    configuration = models.ForeignKey(Configuration, models.DO_NOTHING, blank=False, null=True)
    fw_version = models.ForeignKey(FWVersion, models.DO_NOTHING, blank=False, null=True)
    count = models.BigIntegerField(default=1, blank=True, null=False)
    is_new = models.BooleanField(blank=False, null=False,default=True)
    sold_or_rent = models.BooleanField(blank=False, null=False,default=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'qaime_detail'

    def save(self, *args,**kwargs):
        if not self.id:
            self.created_at=timezone.now()
        self.updated_at=timezone.now()
        return super(QaimeDetail, self).save( *args,**kwargs)

    def __str__(self):
        return self.count
