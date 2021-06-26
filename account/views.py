from django.http import response
from django.shortcuts import render, redirect
from . import forms

# Create your views here.

def register(respone):
    if respone.method == "POST":
        form = forms.RegisterForm(respone.POST)
        if form.is_valid():
            form.save()
        return redirect("/page")
    else:
        form=forms.RegisterForm()

    return render(respone, "register/register.html", {"form":form})
