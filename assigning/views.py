from django.shortcuts import render
from django.http import HttpResponse

from .models import Selection,Exam
from django.core.mail import send_mail
from scheduling.models import Person
# Create your views here.
def selection(request):
    selection_list=Selection.objects.all()
    return render(request,'selection.html',
    {'selection_list':selection_list})

# Create your views here.
def index(request,id):
    list=Selection.objects.get(pk=id)
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

def send(request,exam_Id):
    list = Selection.objects.get(id=1)
    person_list=list.selected_persons.all()
    exam_list=Selection.objects.filter(id=1)
    for exams in exam_list:
        exam_date = exams.exam.date
    email_list=[]
    id_list=[]
    
    for email in person_list:
        email_list.append(email.person.email_Id)
        id_list.append(email.person.id)
    for ids in id_list:
        title=  Person.objects.get(id=ids)
        exam_title=title.person_room.room_no
        person = title.email_Id
        message = 'You have been selected for invigilation of '+exam_title+' on '+str(exam_date)
        send_mail(
            'Hello There',
            message,
            '075bct048.manjeet@pcampus.edu.np',
            [person],
            fail_silently=False,
        )