from django.db import models

from django.contrib import admin
from django.http import request
from scheduling.views import select
from .models import Selection,Exam,Rooms
# Register your models here.

class AssigningAdmin(admin.ModelAdmin):
    list = Exam.objects.get(pk=2)
    manpower = list.manpower
    select(request,manpower)
    list_display=['date','level','manpower']
    """ list_filter=('date','level',) """
    def date(self,obj):
        return obj.exam.date
    def level(self,obj):
        return obj.exam.level
    def manpower(self,obj):
        return obj.exam.manpower
# class SelectionAdmin(admin.ModelAdmin):
  
#     selected_persons = admin.ManyToManyField(Selected_person, default=allpeople)
#     def default_person():
#         list = Person.objects.all().order_by('?')[:10]
#         for items in list:
#             manche = Selection()
#             manche.selected_persons = items
#             manche.selected_persons.save()
class ExamAdmin(admin.ModelAdmin):
    list_display = ('date', 'level', 'manpower')
    list_filter=('date','level',)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('block', 'floor', 'room_no')
    list_filter=('block','floor',)

admin.site.register(Rooms,RoomAdmin)

admin.site.register(Exam,ExamAdmin)
admin.site.register(Selection,AssigningAdmin)