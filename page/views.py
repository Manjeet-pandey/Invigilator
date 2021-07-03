from django.shortcuts import render
from django.template import context, loader
# Create your views here.
from django.http import HttpResponse
from .models import Person

def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('page/side.html')
    # context={
    #     'Hello World'
    # }
    #return HttpResponse(template.render(context,request))
    return render(request, 'web/base.html')

def profile(response, id):
    person_list = Person.objects.get(id=id)
    context={
        "category":person_list.category,
        "first_Name":person_list.first_Name,
        "middle_Name":person_list.middle_Name,
        "last_Name":person_list.last_Name,
        "email_Id": person_list.email_Id,
        "dob":person_list.dob,
        "phone_Num":person_list.phone_Num,
        "gender":person_list.gender,
        "photo":person_list.photo,
        # "field":person_list.field,
        # "highest_Qualification": person_list.highest_Qualification,
        # "college":person_list.college,
    }
    #teacher = person_list.teacher_set.get(id=id)
    # return HttpResponse("<h1>%s</h1><br>" %(person_list.last_Name))
                                                     #str(teacher.highest_Qualification)))
    return render(response, "web/profile.html", {'context':context})

def home(response):
    return render(response, "web/home.html")


