from django.db import models
from exams.models import Exam
from rooms.models import Rooms
from scheduling.models import Person
# Create your models here.
class Selection(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    room_assigned = models.ManyToManyField(Rooms)
    selected_persons = models.ManyToManyField(Person)

    def __str__(self) :
        return str(self.exam.date)
