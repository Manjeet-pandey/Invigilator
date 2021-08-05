
from django import http
from django.http import request,response
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import UserCreationForm

from .forms import RegisterForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            
            form.save()
            return response.HttpResponse()
        else:
            print(form)
            print(form.errors)
            
        return redirect("register/login.html")
    else:
        form=RegisterForm()
    
    return render(request, "register/register.html", {"form":form})

# def login(request):
#     return render(request,"regist/login.html")