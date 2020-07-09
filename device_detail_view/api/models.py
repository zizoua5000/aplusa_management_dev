from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from status.api.models import Status
from simcard.api.models import Simcard
from vehicle.api.models import Vehicle
from company.api.models import Company
from person.api.models import Person
from device_location.api.models import DeviceLocation
from configuration.api.models import Configuration
from project.api.models import Project
from region.api.models import Region
from device_model.api.models import DeviceModel
from device_type.api.models import DeviceType

class DeviceDetailView(models.Model):
    serie = models.CharField(unique=True,max_length=100, blank=False, null=False)
    device_model = models.ForeignKey(DeviceModel, models.DO_NOTHING, blank=False, null=False)
    device_type = models.ForeignKey(DeviceType, models.DO_NOTHING, blank=False, null=False)
    status = models.ForeignKey('status.Status', models.DO_NOTHING, blank=False, null=False)
    simcard = models.ForeignKey('simcard.Simcard', models.DO_NOTHING, blank=True, null=True)
    vehicle = models.ForeignKey('vehicle.Vehicle', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('company.Company', models.DO_NOTHING, blank=True, null=True)
    device_location = models.ForeignKey('device_location.DeviceLocation', models.DO_NOTHING, blank=True, null=True)
    configuration = models.ForeignKey('configuration.Configuration', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('project.Project', models.DO_NOTHING, blank=True, null=True)
    region = models.ForeignKey('region.Region', models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    price_datetime = models.DateTimeField(blank=True, null=True)
    status_datetime = models.DateTimeField(blank=True, null=True)
    sell_count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_detail_view'

    # def save(self, *args,**kwargs):
    #     if not self.id:
    #         # print("---------------------------")
    #         # print(self)
    #         # print("---------------------------")
    #         self.created_at=timezone.now()
    #     self.updated_at=timezone.now()
    #     return super(DeviceDetailView, self).save( *args,**kwargs)

    def __str__(self):
        return self.serie
