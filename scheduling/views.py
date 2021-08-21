from django.http.response import HttpResponse
from .models import Person,Selected_person
from django.shortcuts import render
from exams.models import Exam
from rooms.models import Rooms
from .forms import SelectForm
import random
def select(request,manpower):
    record = Selected_person.objects.all()
    record.delete()
    list = Person.objects.all().order_by('?')[:manpower]
    
    for items in list:
        manche = Selected_person()
        manche.person = items
        manche.save()




def selected (request):

    return render(request, "notice.html",)

