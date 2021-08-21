from django.db import models

# Create your models here.
class Rooms(models.Model):
    block = models.CharField(max_length=30)
    floor = models.CharField(max_length=30)
    room_no = models.CharField(max_length=15)
    def __str__(self):
        return self.room_no