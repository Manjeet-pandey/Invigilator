from django.shortcuts import redirect, render
from django.template import context, loader
# Create your views here.
from django.http import HttpResponse, response
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
    # current_user = request.user
    # id = current_user.id
    # print("fuckkkkkkkkkkkkkkkk", id)
    person_list = Person.objects.get(id=id)
    print(person_list)
    context={
        
        "first_name":person_list.first_name,
        
        "last_name":person_list.last_name,
        "email_Id": person_list.email_Id,
        "dob":person_list.dob,
        "phone_Num":person_list.phone_Num,
        "gender":person_list.gender,
        # "photo":person_list.photo,
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

def profile_id(request):
    current_user = request.user
    print("Profile Id is : ", +current_user.id)
    id = current_user.id
    profile(response,id )

