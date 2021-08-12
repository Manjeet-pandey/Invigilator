from django.shortcuts import redirect, render
from django.template import context, loader
# Create your views here.
from django.http import HttpResponse, response, request
from .models import Person
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'web/index.html')

@login_required
def profile(response, id):
    # current_user = request.user
    # id = current_user.id
    # print("fuckkkkkkkkkkkkkkkk", id)
    person_list = Person.objects.get(id=id)
    print(person_list)

    context={
        
        "first_name":person_list.first_name,
        
        "last_name":person_list.last_name,
        "email": person_list.email,
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

@login_required
def home(response):
    return render(response, "web/home.html")

def profile_id(request):
    current_user = request.user
    print("Profile Id is : ", +current_user.id)
    id = current_user.id
    return redirect('profile',id)

@login_required
def contact(response):
    return render(response, "web/contact.html")



# def error_404_view(request,exception):
#     return render(request, '404.html')
