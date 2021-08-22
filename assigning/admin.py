from django.db import models
from django.contrib.admin import ModelAdmin
from django.contrib import admin
from django.http import request
from scheduling.views import select
from .models import Selection,Exam,Rooms
from django.contrib.admin import ModelAdmin
# Register your models here.


class AssigningAdmin(admin.ModelAdmin):
    # list = Exam.objects.get(id=1)
    # manpower = list.manpower
    # select(request,manpower)
    list_display=['date','level','manpower']
    def rooms(self,obj):
        return obj.selected_persons.all()
    def date(self,obj):
        return obj.exam.date
    def level(self,obj):
        return obj.exam.level
    def manpower(self,obj):
        return obj.exam.manpower
    def block(self,obj):
        return obj.room_assigned.block
    
    
    def save_related(self, request, form, formsets, change):
        
        form.save_m2m()
        for formset in formsets:
            self.save_formset(request, form, formset, change=change)
    
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