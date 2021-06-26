# from django.shortcuts import render
# from django.template import context, loader
# # Create your views here.
# from django.http import HttpResponse
# # from .models import Teacher, Staff, Student


# def index(request):
#     #latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     #template = loader.get_template('page/side.html')
#     # context={
#     #     'Hello World'
#     # }
#     #return HttpResponse(template.render(context,request))
#     return render(request, 'web/side.html')

# def profile(request):
#     value = Teacher.objects.order_by()
#     context = {"value":value }
#     #return HttpResponse(display(value))
#     return render(request, 'web/profile.html',context)

