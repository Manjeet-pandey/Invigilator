from django.db import models
from django.db.models.fields.related import ManyToManyField
from scheduling.models import Selected_person
from django.contrib import admin
from .models import Selection
from django.http import request
from scheduling.views import select, selected
from scheduling.models import Person
from .models import Selection
from exams.models import Exam
# Register your models here.
list = Exam.objects.get(pk=1)
manpower = list.manpower
select(request,manpower)
# class SelectionAdmin(admin.ModelAdmin):
  
#     selected_persons = admin.ManyToManyField(Selected_person, default=allpeople)
#     def default_person():
#         list = Person.objects.all().order_by('?')[:10]
#         for items in list:
#             manche = Selection()
#             manche.selected_persons = items
#             manche.selected_persons.save()

admin.site.register(Selection)