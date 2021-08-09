
from page.models import Person
from django.db import models
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

#from crispy_forms import *


class RegisterForm(UserCreationForm):
    class Meta:
        model = Person
        fields = [ "username" ,"first_name" ,"last_name","email",
                  "dob", "gender", "phone_Num","photo","password1","password2"]

        def __init__(self, *args, **kwargs):
            super(RegisterForm, self).__init__(*args, **kwargs)
            self.fields['photo'].required = False


        # REQUIRED_FIELDS = ["first_Name", "last_Name","e,ail"
        #               "dob", "gender", "phone_Num", "photo"]
 
 
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

# class Update_profile(ModelForm):
    
#     class Meta:
#         model = Person
#         fields = [ "username" ,"first_name" ,"last_name","email",
#                   "dob", "gender", "phone_Num","photo","password1","password2"]