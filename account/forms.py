<<<<<<< HEAD
from account.models import Teacher
# from django import forms
=======
from page.models import Person
from django.db import models
from django import forms
>>>>>>> 68aaa912b49e59c34adeb985210c8d5244e39c13
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from crispy_forms import *


class RegisterForm(UserCreationForm):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    #def TeacherForm():
    uid = models.UUIDField(
        default=None,
        blank=True,
        null=True,
        unique=True,
    )

    class Meta:
        model = Person
        fields = ["category", "first_Name", "middle_Name", "last_Name",
                  "dob", "gender", "phone_Num", "photo"]

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["category", "first_Name", "last_Name",
                       "dob", "gender", "phone_Num", "photo"]

    def __str__(self):
        return self.email
    
<<<<<<< HEAD
    def TeacherForm():
        class Meta:
            models = Teacher
            fields = ["first_Name", "middle_Name", "last_Name", "dob", "phone_Num", "gender",
                    "qualification", "photo", "email_Id"]
=======
>>>>>>> 68aaa912b49e59c34adeb985210c8d5244e39c13
    

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
