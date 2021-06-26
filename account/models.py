from django.db import models
from django.db.models.aggregates import Max
from phonenumber_field.modelfields import PhoneNumberField
#from django import forms
#from typing_extensions import Required

# Create your models here.


class Teacher(models.Model):
    first_Name = models.CharField(max_length=50)
    middle_Name = models.CharField(max_length=50, blank=True)
    last_Name = models.CharField(max_length=50)
    email_Id = models.EmailField('email_Id', blank=True)
    dob = models.DateField('dob', blank=True)
    phone_Num = PhoneNumberField(name = 'phone_Num', blank=True)
    gender = models.BooleanField('gender', blank=True)
    phone_Num = models.CharField(max_length=10,name='phone_Num')
    gender = models.BooleanField('gender', blank=True)
    highest_Qualification = models.CharField(max_length=50, name='qualification', blank=True)
    photo = models.ImageField('photo', blank=True)
    #profileId = last_Name+first_Name


class Staff(models.Model):
    first_Name = models.CharField(max_length=50)
    middle_Name = models.CharField(max_length=50)
    last_Name = models.CharField(max_length=50)
    email_Id = models.EmailField('email_Id')
    dob = models.DateField('dob')
    phone_Num = models.CharField(max_length=10, name='phone_Num')
    gender = models.BooleanField('gender')
    field = models.CharField(max_length=15, name='field')
    photo = models.ImageField('photo')
    #profileId = last_Name+first_Name


class Student(models.Model):
    first_Name = models.CharField(max_length=50)
    middle_Name = models.CharField(max_length=50)
    last_Name = models.CharField(max_length=50)
    email_Id = models.EmailField('email_Id')
    dob = models.DateField('dob')
    phone_Num = models.CharField(max_length=10, name='phone_Num')
    gender = models.BooleanField('gender')
    highest_Qualification = models.CharField(
        max_length=50, name='qualification')
    college = models.CharField(max_length=20, name='college')
    photo = models.ImageField('photo')
    #profileId = last_Name+first_Name

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
