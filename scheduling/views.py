from django.http.response import HttpResponse
from .models import Person,Selected_person
from django.shortcuts import render
from .forms import LoginForm
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import random

def select(request,manpower):
    record = Selected_person.objects.all()
    record.delete()
    list = Person.objects.all().order_by('?')[:manpower]
    for items in list:
        manche = Selected_person()
        manche.person = items
        manche.save()

def authenticate(username,password):
    email_Id=username
    if Person.objects.filter(email_Id=email_Id).exists():
        if password == '123456':
            return True
    
    


def login(request):

    form = LoginForm(request.POST)
    if request.POST:
        
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
                return HttpResponseRedirect('/index')
    return render(request,'login.html')

# def selected (request):

#     #form to input a new student
#     form = SelectForm(request.POST or None) 

#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save() 

#     context = { 
#         "form":form
#     }

#     return render(request, "table.html", context)
