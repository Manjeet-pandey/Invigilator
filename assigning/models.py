from django.db import models
from exams.models import Exam
from rooms.models import Rooms
from scheduling.models import Selected_person
# Create your models here.
class Selection(models.Model):
    def allpeople():
        list= Selected_person.objects.all()
        return list
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    room_assigned = models.ManyToManyField(Rooms)
    selected_persons = models.ManyToManyField(Selected_person,default=allpeople)

    def __str__(self) :
        return str(self.exam.date)
