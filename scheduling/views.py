from django.http.response import HttpResponse
from .models import Person
from django.shortcuts import render
import random
def select(response):
    list = Person.objects.all().order_by('?')[:10]
    print(list)
    return render(response, "table.html", {'list':list})
