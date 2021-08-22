

from assigning.models import Selection
from .models import Person,Selected_person,Notice
from django.shortcuts import render
from .forms import LoginForm
from django.shortcuts import render,redirect
from assigning.views import index

def select(request,manpower):
    record = Selected_person.objects.all()
    record.delete()
    list = Person.objects.all().order_by('?')[:manpower]
    for items in list:
        manche = Selected_person()
        manche.person = items
        manche.save()

def authenticate(username,password):
    email_Id=username
    if Person.objects.filter(email_Id=email_Id).exists():
        if password == '123456':
            return True
    
    
def notice(request):
    noticelist=Notice.objects.all()
    return render(request,'notice.html',{'noticelist':noticelist})
def login(request):
    form = LoginForm(request.POST)
    if request.POST:
        
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
                selected = Selection.objects.get(pk=1)
                people = selected.selected_persons.get(person=username)
                id = people.id
                print(id)
                return index(request,id)
    return render(request,'login.html')

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
