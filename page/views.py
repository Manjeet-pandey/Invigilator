from django.shortcuts import render
from django.template import context, loader
# Create your views here.
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('page/side.html')
    context={
        'Hello World': latest_question_list,
    }
    #return HttpResponse(template.render(context,request))
    return render(request, 'web/side.html', context)