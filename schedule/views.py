from page.models import Person
from django.shortcuts import render,redirect
from .models import Schedule
from django.contrib import messages
from .forms import Add_schedule


from django.contrib.auth import authenticate 

# Create your views here.
def schedule(request):
    scheduling = Schedule.objects.get(pk=1)
    context={
        "title_name" : scheduling.title,
        "date": scheduling.date,
        "time": scheduling.time,

    }
    return render(request,"schedule.html",{'context':context})

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
            # print(form)
            # print(form.errors)
        redirect('register')
            
        
    else:
        form=Add_schedule()
    
    return render(request, "add_schedule.html", {"form":form})

def get_id(request):
    current_user = request.user
    return current_user.id
