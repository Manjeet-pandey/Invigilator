from django.db import models
from django import forms
from django.db.models import fields

class ExamForm(forms.ModelForm):
    class Meta:
        fields=('date','level','manpower')