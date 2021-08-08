from django.core.exceptions import ValidationError
from django import forms
from django.forms import ModelForm, widgets
from .models import  Schedule, TITLE_CHOICES
DATE_CHOICES = [
    ('1', '06'),
    ('2', '2057-03-06'),
    ('3', '2057-04-06'),
]
TIME_CHOICES = [
    ('6:00','6am'),
    ('7:00','7am'),
    ('8:00','8am')
]
class Add_schedule(ModelForm):
    date=forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices=DATE_CHOICES,)
    time=forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices=TIME_CHOICES)
    class Meta:
        model = Schedule
        fields =["name","title","date","time"]
        widgets = {"name":forms.HiddenInput}
        #unique_together =(('name','title','date','time'))
        # def Add_schedule(self):
        #     title= self.cleaned_data['name']
        #     # title= self.cleaned_data['title']
        #     # date= self.cleaned_data['date']
        #     # time= self.cleaned_data['time']
        #     if Schedule.objects.filter(title=title).exists():
        #         raise ValidationError("Name Already exists")
        #     return title

class Update(ModelForm):
    date=forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices=DATE_CHOICES)
    time=forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices=TIME_CHOICES)
    class Meta:
        model = Schedule
        fields =["title","date","time"]
        