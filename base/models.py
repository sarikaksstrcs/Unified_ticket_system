from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True,blank=True)
    event_name = models.CharField(max_length=200)
    event_date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    parking = models.BooleanField(default=False)
    parking_capacity = models.PositiveIntegerField()
    tickets_available = models.PositiveIntegerField()
    tickets_sold = models.PositiveIntegerField()
    complete = models.BooleanField(default= False)
    booking_open = models.BooleanField(default=True)
    
    def __str__(self):
        return self.event_name
    
    
