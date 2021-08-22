from django.shortcuts import render
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