from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from company.api.models import Company
from device_model.api.models import DeviceModel
from device_type.api.models import DeviceType
from device_detail.api.models import DeviceDetail

class Device(models.Model):
    serie = models.CharField(unique=True,max_length=100, blank=False, null=False)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    device_model = models.ForeignKey(DeviceModel, models.DO_NOTHING, blank=False, null=False)
    device_type = models.ForeignKey(DeviceType, models.DO_NOTHING, blank=False, null=False)
    device_detail = models.ForeignKey(DeviceDetail, models.DO_NOTHING, blank=False, null=False)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    deleted_at = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'device'

    def save(self, *args,**kwargs):
        if not self.id:
            self.created_at=timezone.now()
        self.updated_at=timezone.now()
        return super(Device, self).save( *args,**kwargs)

    def __str__(self):
        return self.serie
