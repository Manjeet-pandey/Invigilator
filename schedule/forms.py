from django.core.exceptions import ValidationError
from django import forms
from django.forms import ModelForm, widgets
from .models import Schedule
class Add_schedule(ModelForm):
    class Meta:
        model = Schedule
        fields =["name","title","date","time"]
        widgets = {"name":forms.HiddenInput}
        #unique_together =(('name','title','date','time'))
        def Add_schedule(self):
            title= self.cleaned_data['name']
            # title= self.cleaned_data['title']
            # date= self.cleaned_data['date']
            # time= self.cleaned_data['time']
            if Schedule.objects.filter(title=title).exists():
                raise ValidationError("Name Already exists")
            return title

