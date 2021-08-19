from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser,BaseUserManager
from rooms.models import Rooms
from exams.models import Exam
class Person(models.Model):

    first_Name = models.CharField('first_Name',max_length=50)
    last_Name = models.CharField('last_Name', max_length=50)
    gender = models.CharField('gender', max_length=5,blank=False)
    age = models.CharField('age',max_length=3)
    email_Id = models.CharField('email_Id',max_length=20)
    
    phone_Num = models.CharField('phone_Num', max_length=10,)
    
    # photo = models.ImageField('photo', upload_to='photo_Uploads', null=True, blank=True)
    # dob = models.DateField('dob', null=True)
   # password = models.CharField('password', max_length=50)
    # qualification = models.CharField(max_length=15,widgets=forms.HiddenInput(),required=False, name='qualification
    # ')
    # def categ(category):
    #     if category=='S':
            
        #     return  models.CharField(max_length=15, name='field')
        # elif category=='T':
        #    return  models.CharField(
        #         max_length=50, name='qualification')
        # elif category=='O':
        #     highest_Qualification = models.CharField(
        #         max_length=50, name='qualification')
        #     college = models.CharField(max_length=20, name='college')
        # else:
        #     pass
    # field = models.CharField(max_length=15,default=categ(category))
    
   
    def __str__(self):
        return self.first_Name

class Selected_person(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    rooms_assigned = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    def __str__(self):
        return self.person.first_Name