
from django.db import models
from django import forms
class Rooms(models.Model):
    block = models.CharField(max_length=30)
    floor = models.CharField(max_length=30)
    room_no = models.CharField(max_length=15)
    def __str__(self):
        return self.room_no
class Person(models.Model):

    first_Name = models.CharField('first_Name',max_length=50)
    last_Name = models.CharField('last_Name', max_length=50)
    gender = models.CharField('gender', max_length=50,blank=False)
    age = models.CharField('age',max_length=3)
    email_Id = models.CharField('email_Id',max_length=50)
    phone_Num = models.CharField('phone_Num', max_length=100)
    person_room = models.ForeignKey(Rooms, null=True, on_delete=models.CASCADE)
#     #password = None
#     #date_joined, gender, age, email_Id, phone_Num
   
#     #password = models.CharField('password', max_length=50)
#     # photo = models.ImageField('photo', upload_to='photo_Uploads', null=True, blank=True)
#     # dob = models.DateField('dob', null=True)
#    # password = models.CharField('password', max_length=50)
#     # qualification = models.CharField(max_length=15,widgets=forms.HiddenInput(),required=False, name='qualification
#     # ')
#     # def categ(category):
#     #     if category=='S':
            
#         #     return  models.CharField(max_length=15, name='field')
#         # elif category=='T':
#         #    return  models.CharField(
#         #         max_length=50, name='qualification')
#         # elif category=='O':
#         #     highest_Qualification = models.CharField(
#         #         max_length=50, name='qualification')
#         #     college = models.CharField(max_length=20, name='college')
#         # else:
#         #     pass
#     # field = models.CharField(max_length=15,default=categ(category))
    
   
    def __str__(self):
        return self.first_Name

class Selected_person(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    def __str__(self):
        return self.person.first_Name

class Notice(models.Model):
    notice_upload = models.ImageField(upload_to= 'noticeUpload/', null=True , blank=True)
    description = models.CharField(max_length=150,null=True)
    def __str__(self):
        return self.description