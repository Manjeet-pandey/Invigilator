from django.db import models

from scheduling.models import Selected_person,Rooms
# Create your models he

class Exam(models.Model):
    date = models.DateField('date')
    level = models.CharField(max_length=15)
    manpower = models.PositiveSmallIntegerField()
    def __str__(self):
        return str(self.level)

# class Rooms(models.Model):
#     block = models.CharField(max_length=30)
#     floor = models.CharField(max_length=30)
#     room_no = models.CharField(max_length=15)
#     def __str__(self):
        # return self.room_no
class  Selection(models.Model):
    def allpeople():
        list= Selected_person.objects.all()
        return list
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    room_assigned = models.ManyToManyField(Rooms)
    selected_persons = models.ManyToManyField(Selected_person,default=allpeople)

    def __str__(self):
        return str(self.exam.date)