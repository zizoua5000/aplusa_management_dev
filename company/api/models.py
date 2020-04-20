from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from company_type.api.models import CompanyType

class Company(models.Model):
    main_company = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    deleted_at = models.DateTimeField(editable=False)
    name = models.CharField(unique=True,max_length=200, blank=False, null=False)
    company_type = models.ForeignKey('company_type.CompanyType', models.DO_NOTHING, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'company'

    def save(self, *args,**kwargs):
        if not self.id:
            self.created_at=timezone.now()
        self.updated_at=timezone.now()
        return super(Company, self).save( *args,**kwargs)

    def __str__(self):
        return self.name
