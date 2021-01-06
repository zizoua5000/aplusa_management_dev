from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from company.api.models import Company
from department.api.models import Department
from job_title.api.models import JobTitle
from django.contrib.auth.models import User

class Person(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    phone = models.CharField(unique=True,max_length=15, blank=True, null=True)
    email = models.CharField(unique=True,max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to='media/person/', blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=False, null=False)
    department = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    job_title = models.ForeignKey(JobTitle, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, unique=True,blank=True, null=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    deleted_at = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'person'
        # unique_together = (('user', 'permission'),)

    def save(self, *args,**kwargs):
        if not self.id:
            self.created_at=timezone.now()
        self.updated_at=timezone.now()

        
        if self.id and not self.photo:
            self.photo=self.get_already_exist_person_photo()
        self.photo=self.photo
        return super(Person, self).save( *args,**kwargs)

    def __str__(self):
        return self.first_name + self.last_name
    
    def get_already_exist_person_photo(self):
        return Person.objects.get(id=self.id).photo

