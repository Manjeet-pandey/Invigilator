from django.http.response import HttpResponse
from page.models import Person
from django.shortcuts import render,redirect
from .models import Schedule
from django.contrib import messages
from .forms import Add_schedule, Update
import hashlib

from django.contrib.auth import authenticate 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def schedule(request):
    name = request.user
    scheduling = Schedule.objects.filter(name=request.user)
    
    
    return render(request,"schedule.html",{'scheduling':scheduling})


@login_required
def add_schedule(request):
    if request.method == "POST":
        form = Add_schedule(request.POST)
        
        if form.is_valid():
            
            schedule_form=form.save(commit=False)
            schedule_form.name = request.user
            schedule_form.save()
            messages.success(request,"Schedule Added Successfully")
            return redirect("/schedule")

        # else:
        #     print(form)
        #     print(form.errors)
        redirect('/schedule')
            
        
    else:
        form=Add_schedule()
    
    return render(request, "add_schedule.html", {"form":form})

def get_id(request):
   
    return redirect('update_schedule',id)
def del_schedule(request,id):
    date = Schedule.objects.get(pk=id)
    date.delete()
    messages.success(request,"Schedule Deleted Successfully")
    return redirect("/schedule/view")

def update_schedule(request,id):
    data = Schedule.objects.get(pk=id)
    form = Update(instance=data)
    if request.method == "POST":
        scheduleadd = Update(request.POST, instance=data)
       
        if scheduleadd.is_valid():
            scheduleadd.save()
            messages.success(request,"Schedule Updated Successfully")
            return redirect("/schedule/view")
        else:
            print(form)
            print(form.errors)
    return render(request, "update_schedule.html", {"form":form,
    "data":data
    })

    

