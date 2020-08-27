from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from company.api.models import Company
from device_model.api.models import DeviceModel
from device_type.api.models import DeviceType
from status.api.models import Status 
from person.api.models import Person
from vehicle.api.models import Vehicle
from device_location.api.models import DeviceLocation
from configuration.api.models import Configuration
from project.api.models import Project
from fw_version.api.models import FWVersion
from simcard.api.models import Simcard

class DeviceHistory(models.Model):
    serie = models.CharField(unique=True,max_length=100, blank=False, null=False)
    company = models.ForeignKey(Company, models.DO_NOTHING,related_name='device_history_company', blank=True, null=True)
    device_model = models.ForeignKey(DeviceModel, models.DO_NOTHING, blank=False, null=False)
    device_type = models.ForeignKey(DeviceType, models.DO_NOTHING, blank=False, null=False)
    manufacturer = models.ForeignKey(Company, models.DO_NOTHING,related_name='device_history_manufacturer', blank=True, null=True)
    status = models.ForeignKey(Status, models.DO_NOTHING,related_name='device_history_status', blank=False, null=False)
    simcard = models.ForeignKey(Simcard, models.DO_NOTHING, blank=True, null=True)
    vehicle = models.ForeignKey(Vehicle, models.DO_NOTHING, blank=True, null=True)
    recipient = models.ForeignKey(Person, models.DO_NOTHING, unique=True,  blank=True, null=True)
    device_location = models.ForeignKey(DeviceLocation, models.DO_NOTHING, blank=True, null=True)
    configuration = models.ForeignKey(Configuration, models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey(Project, models.DO_NOTHING, blank=True, null=True)
    fw_version = models.ForeignKey(FWVersion, models.DO_NOTHING, blank=True, null=True)
    sell_count = models.BigIntegerField(blank=True, null=True)
    rated_price = models.FloatField(blank=False, null=False)
    guarantee_to_us = models.DateTimeField(blank=True, null=True)
    guarantee_from_us = models.DateTimeField(blank=True, null=True)
    manufacture_date = models.DateTimeField(blank=True, null=True)
    buy_date = models.DateTimeField(blank=True, null=True)
    entry_warehouse_date = models.DateTimeField(blank=True, null=True)
    webtrack_status = models.ForeignKey(Status, models.DO_NOTHING,related_name='device_history_webtrack_status', blank=False, null=False)
    is_our = models.BooleanField(blank=False, null=False)
    is_rent = models.BooleanField(blank=False, null=False)
    is_sold = models.BooleanField(blank=False, null=False)
    sell_price = models.FloatField(blank=False, null=False)
    device_event_datetime = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    deleted_at = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'device_history'

    def save(self, *args,**kwargs):
        
        if not self.id:
            
            self.created_at=timezone.now()
        self.updated_at=timezone.now()
        return super(DeviceHistory, self).save( *args,**kwargs)

    def __str__(self):
        return self.serie
