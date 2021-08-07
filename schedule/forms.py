
from django import forms
from django.forms import ModelForm, widgets
from .models import Schedule
class Add_schedule(ModelForm):
    class Meta:
        model = Schedule
        fields =["name","title","date","time"]
        widgets = {"name":forms.HiddenInput}

