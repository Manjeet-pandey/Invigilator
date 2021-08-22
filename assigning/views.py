from django.shortcuts import render
from django.http import HttpResponse
from .models import Selection

# Create your views here.
def selection(request):
    selection_list=Selection.objects.all()
    return render(request,'selection.html',
    {'selection_list':selection_list})
from .models import Selection
# Create your views here.
def index(request):
    list=Selection.objects.get(id=1)
    persons= list.selected_persons.all()
    for person in persons:
       people = person.person.first_Name
    context={
        "exam_date":list.exam.date,
        "exam_level":list.exam.level,
        "people":people,
        
        #"room":list.room_assigned.block
    }
    
    return render (request,"table.html",{'context':context})
