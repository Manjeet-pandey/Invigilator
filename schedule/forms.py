
from django.forms import ModelForm
from .models import Schedule
class Add_schedule(ModelForm):
    class Meta:
        model = Schedule
        fields =["title","date","time"]

