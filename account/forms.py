from page.models import Person
from django.db import models
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
#from crispy_forms import *


class RegisterForm(UserCreationForm):
    class Meta:
        model = Person
        fields = ["category", "first_Name", "middle_Name", "last_Name",
                  "email_Id", "dob", "gender", "phone_Num", "photo"]
        #model.save()
    # REQUIRED_FIELDS = ["category", "first_Name", "last_Name",
    #                    "email", "dob", "gender", "phone_Num", "photo"]

# class LoginForm(UserCreationForm):
#     class Meta:
        

    # def StaffForm():
    #     class Meta:
    #         model = Teacher
    #         fields = ["first_Name", "middle_Name", "last_Name", "dob", "phone_Num", "gender",
    #                   "qualification", "photo", "email_Id"]

    # def StudentForm():
    #     class Meta:
    #         model = Teacher
    #         fields = ["first_Name", "middle_Name", "last_Name", "dob", "phone_Num", "gender",
    #                   "qualification", "photo", "email_Id"]
