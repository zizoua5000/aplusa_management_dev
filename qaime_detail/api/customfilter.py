from django_filters import rest_framework as filter
from datetime import datetime, timedelta

class DateListFilter(filter.Filter):
    def filter(self,qs,value):
        if value not in (None,''):
            dates = [v for v in value.split(',')]
            lg = len(dates)
            if dates[lg-1]=='':
                dates.pop(lg-1)
            
            qs_set = qs.all()
            for obj in qs_set.iterator():
                four_hours_from_datetime=obj.start_datetime + timedelta(hours=4)

            return qs.filter(**{'%s__%s'%(self.field_name,self.lookup_expr):dates})
        return qs