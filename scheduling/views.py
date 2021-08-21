from django.http.response import HttpResponse
from .models import Person,Selected_person
from django.shortcuts import render
from exams.models import Exam
from rooms.models import Rooms
from .forms import SelectForm
import random
def select(response):
    list = Person.objects.all().order_by('?')[:10]
    dates = Exam.objects.all()
    kotha = Rooms.objects.all()
    
    for items in list:
        manche = Selected_person()
        manche.person = items

        for room in kotha:
            manche.rooms_assigned = room
        for date in dates:
            manche.exam  = date
        manche.save()
    
    
    
    
    return render(response, "table.html", {'list':list})



def selected (request):

    #form to input a new student
    form = SelectForm(request.POST or None) 

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save() 

    context = { 
        "form":form
    }

    return render(request, "table.html", context)