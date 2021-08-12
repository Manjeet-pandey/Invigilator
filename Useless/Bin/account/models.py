from django.db import models
from django.db.models.aggregates import Max

#phone number
from django.core.validators import MinLengthValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
#from django import forms
#from typing_extensions import Required

# Create your models here.
# class User(AbstractUser):
#     USER_TYPE_CHOICES = (
#         (1, 'student'),
#         (2, 'staff'),
#         (3, 'teacher'),
#     )
#     user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)


class Teacher(models.Model):
    first_Name = models.CharField(max_length=50)
    middle_Name = models.CharField('middle_Name', max_length=50)
    last_Name = models.CharField('last_Name', max_length=50)
    email_Id = models.EmailField('email_Id')
    dob = models.DateField('dob')
    #phone_Num = PhoneNumberField(name = 'phone_Num', blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Others'),
    )
    gender = models.CharField('gender', max_length=1, choices=GENDER_CHOICES),
    phone_Num = models.CharField('phone_Num', max_length=10, validators=[
        MinLengthValidator(10)])
    photo = models.ImageField('photo')

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

