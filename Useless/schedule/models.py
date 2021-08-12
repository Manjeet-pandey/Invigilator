
from django.db import models
from django.db.models import query
from django.db.models.fields import DateField
from django.forms import ModelForm
from django import forms

from page.models import Person

# Create your models here.
TITLE_CHOICES = [
    ('M','Masters'),
    ('B','Bachelors'),
    ('E','Entrance'),
    ]


class Schedule(models.Model):
    # current_user = request.user
    # id = current_user.id
    #user_id = models.CharField(max_length=10,null=True)
    name = models.CharField(max_length=20,blank=True)
    title = models.CharField(max_length=10,choices=TITLE_CHOICES)
    date = models.CharField(max_length=30)
    time = models.CharField('time', max_length=30)

    def __str__(self):
        return self.name
