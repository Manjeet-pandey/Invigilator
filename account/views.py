from django.http import response
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .forms import RegisterForm

# Create your views here.

def register(respone):
    if respone.method == "POST":
        form = RegisterForm(respone.POST)
        if form.is_valid():
            form.save()
            return response.HttpResponse()
        return redirect("/profile/1")
    else:
        form=RegisterForm(response)
    
    return render(respone, "register/register.html", {"form":form})
