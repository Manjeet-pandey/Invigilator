
from django import http
from django.http import request,response
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import UserCreationForm
from page.models import Person
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
# def update_profile(request,id):
#     data = Person.objects.get(pk=id)
#     form = Update_profile(instance=data)
#     if request.method == "POST":
#         profile = Update_profile(request.POST, instance=data)
       
#         if profile.is_valid():
#             profile.save()
#             messages.success(request,"Profile Updated Successfully")
#             return redirect("/profile_Id")
#         else:
#             print(form)
#             print(form.errors)
#     return render(request, "update_schedule.html", {"form":form,
#     "data":data
#     })
