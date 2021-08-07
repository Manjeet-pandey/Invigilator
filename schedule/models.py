from django.db import models
from django.forms import ModelForm
from django.db.models.fields import CharField
from django.db.models.aggregates import Max
# Create your models here.
TITLE_CHOICES = [
    ('M','Masters'),
    ('B','Bachelors'),
    ('E','Entrance'),
    ]
class Schedule(models.Model):
    
    title = models.CharField(max_length=10,choices=TITLE_CHOICES)
    date = models.DateField('date') 
    time = models.TimeField('time')

    def __str__(self):
        return self.title
