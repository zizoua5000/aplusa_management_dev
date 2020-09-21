from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

class CurrencyRate(models.Model):

    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(editable=False)

    class Meta:
        managed = False
        db_table = 'currency_rate'

    def save(self, *args,**kwargs):
        if not self.id:
            self.created_at=timezone.now()
        self.updated_at=timezone.now()
        return super(CurrencyRate, self).save( *args,**kwargs)

    # def __str__(self):
    #     return self.action.name
