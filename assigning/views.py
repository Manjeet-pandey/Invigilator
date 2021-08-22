from django.shortcuts import render
from django.http import HttpResponse
from .models import Selection

# Create your views here.
def selection(request):
    selection_list=Selection.objects.all()
    return render(request,'selection.html',
    {'selection_list':selection_list})
