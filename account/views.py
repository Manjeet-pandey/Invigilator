
from django import http
from django.http import request,response
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import UserCreationForm

from .forms import RegisterForm

# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return redirect("/login")

        # else:
            # print(form)
            # print(form.errors)
        redirect('register')

    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form": form})

# def login(request):
#     return render(request,"regist/login.html")
