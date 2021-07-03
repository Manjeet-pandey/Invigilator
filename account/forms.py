from account.models import Teacher
# from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from crispy_forms import *


class RegisterForm(ModelForm):
    
    def TeacherForm():
        class Meta:
            models = Teacher
            fields = ["first_Name", "middle_Name", "last_Name", "dob", "phone_Num", "gender",
                    "qualification", "photo", "email_Id"]
    
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
