from datetime import datetime
from urllib import request
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from random import randint,randrange


inc_status=(
    ('open','open'),('in progress','in progress'),('closed','closed')
)
inc_priority=(
    ('low',"low"),('medium','medium'),('high','high')
)
def incident_no():
        return 'RMG'+str(randint(10000,99999)) + str(datetime.now().year)



class incident(models.Model):
    incident_number = models.CharField(unique=True,max_length=12,editable=False)
    reporter_name = models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
    incident_details = models.TextField(null=False,blank=False,editable=True)
    priority =  models.CharField(max_length=6,choices=inc_priority,default='high',editable=True)
    incident_status = models.CharField(max_length=11,choices=inc_status,default='open',editable=True)
    reported_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.incident_number

    


    

    def save(self,*args,**kwargs):
        self.incident_number=incident_no()
        super(incident,self).save(*args,**kwargs)
    
    

    