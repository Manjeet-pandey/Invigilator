from django.db import models
from django.db.models.fields import DateField

# Create your models here.
class Exam(models.Model):
    date = models.DateField('date')
    level = models.CharField(max_length=15)
    manpower = models.PositiveSmallIntegerField()
    def __str__(self):
        return str(self.date)