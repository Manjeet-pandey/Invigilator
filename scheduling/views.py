from django.http.response import HttpResponse
from .models import Person,Selected_person
from django.shortcuts import render

import random
def select(request,manpower):
    record = Selected_person.objects.all()
    record.delete()
    list = Person.objects.all().order_by('?')[:manpower]
    
    for items in list:
        manche = Selected_person()
        manche.person = items
        manche.save()




# def selected (request):

#     #form to input a new student
#     form = SelectForm(request.POST or None) 

#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save() 

#     context = { 
#         "form":form
#     }

#     return render(request, "table.html", context)