from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from project.api.models import Project
from company.api.models import Company

class MProjectCompany(models.Model):
    project = models.ForeignKey(Project, models.DO_NOTHING, blank=False, null=False)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=False, null=False)
    created_at = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'm_project_company'

    def save(self, *args,**kwargs):
        if not self.id:
            self.created_at=timezone.now()
        self.updated_at=timezone.now()
        return super(MProjectCompany, self).save( *args,**kwargs)

    def __str__(self):
        return self.project

