from django.db import models
from django.db.models.aggregates import Max

from django.core.validators import MinLengthValidator
from phonenumber_field.modelfields import PhoneNumberField
#from django import forms
#from typing_extensions import Required

# Create your models here.

class Person(models.Model):

    CATEGORY_CHOICES = (
        ('T', 'Teacher'),
        ('S', 'Staff'),
        ('O', 'Other'),
    )
    category = models.CharField('category', max_length=1, choices=CATEGORY_CHOICES)

    first_Name = models.CharField(max_length=50)
    middle_Name = models.CharField('middle_Name', max_length=50)
    last_Name = models.CharField('last_Name', max_length=50)
    email_Id = models.EmailField('email_Id')
    dob = models.DateField('dob')
    phone_Num = PhoneNumberField(name = 'phone_Num', blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Others'),
    )
    gender = models.CharField('gender', max_length=1, choices=GENDER_CHOICES),
    phone_Num = models.CharField('phone_Num', max_length=10, validators=[MinLengthValidator(10)])
    photo = models.ImageField('photo', upload_to='image_Uploads')

    if category=='S':
        field = models.CharField(max_length=15, name='field')
    else:
        if category=='T':
            highest_Qualification = models.CharField(
                max_length=50, name='qualification')
        else:
            college = models.CharField(max_length=20, name='college')

    def __str__(self):
        return self.last_Name

# class Teacher(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     first_Name = models.CharField('first_Name', max_length=50)
#     middle_Name = models.CharField('middle_Name', max_length=50)
#     last_Name = models.CharField('last_Name', max_length=50)
#     email_Id = models.EmailField('email_Id')
#     dob = models.DateField('dob')
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('N', 'Others'),
#     )
#     gender = models.CharField('gender', max_length=1, choices=GENDER_CHOICES),
#     phone_Num = models.CharField('phone_Num', max_length=10, validators=[
#                                  MinLengthValidator(10)])
#     photo = models.ImageField('photo', upload_to='image_Uploads')
#     highest_Qualification = models.CharField(
#         'highest_Qualification', max_length=50)
#     # photo = models.ImageField('photo', blank=True)
#     #profileId = last_Name + first_Name

#     def __str__(self):
#         return self.last_Name


# class Staff(models.Model):
# #     first_Name = models.CharField(max_length=50)
# #     middle_Name = models.CharField(max_length=50)
# #     last_Name = models.CharField(max_length=50)
# #     email_Id = models.EmailField('email_Id')
# #     dob = models.DateField('dob')
# #     phone_Num = models.CharField(max_length=10, name='phone_Num')
# #     gender = models.BooleanField('gender')
#     field = models.CharField(max_length=15, name='field')
# #     photo = models.ImageField('photo')
# #     #profileId = last_Name+first_Name


# class Student(models.Model):
# #     first_Name = models.CharField(max_length=50)
# #     middle_Name = models.CharField(max_length=50)
# #     last_Name = models.CharField(max_length=50)
# #     email_Id = models.EmailField('email_Id')
# #     dob = models.DateField('dob')
# #     phone_Num = models.CharField(max_length=10,name='phone_Num')
# #     gender = models.BooleanField('gender')
#     highest_Qualification = models.CharField(max_length=50, name='qualification')
#     college = models.CharField(max_length=20, name='college')
# #     photo = models.ImageField('photo')
# #     #profileId = last_Name+first_Name

# # class Choice(models.Model):
# #     question = models.ForeignKey(Question, on_delete=models.CASCADE)
# #     choice_text = models.CharField(max_length=200)
# #     votes = models.IntegerField(default=0)
