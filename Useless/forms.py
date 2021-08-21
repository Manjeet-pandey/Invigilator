from django.db.models import fields
from .models import Notice, Selected_person,Person
from django.db import models
from django import forms
from django.forms import ModelForm,ModelChoiceField


class SelectForm(forms.ModelForm):
    person = forms.ModelChoiceField(queryset=Person.objects.all(), initial=0)
    rooms_assigned = forms.ModelChoiceField(queryset=Rooms.objects.all(), initial=0)
    exam = forms.ModelChoiceField(queryset=Exam.objects.all(), initial=0)
    class Meta:
        model = Selected_person
        fields = ('person', 'rooms_assigned', 'exam')

class addNotice(forms.ModelForm):
    class Meta:
        model=Notice
        fields= ('notice_upload','description',)
        
