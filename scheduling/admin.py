from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import  Person, Selected_person
    
class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       list_display=('first_Name','last_Name','age','gender','email_Id','phone_Num')
       search_fields=('first_Name','last_Name','age','gender','email_Id','phone_Num')
       class Meta:
           model =Person
class SelectedAdmin(admin.ModelAdmin):
    list_display=('first_Name',)
    def first_Name(self,obj):
        return obj.person.first_Name
    def room_no(self,obj):
        return obj.rooms_assigned.room_no
    def date(self,obj):
        return obj.exam.date
admin.site.register(Person, BlogAdmin)
admin.site.register(Selected_person,SelectedAdmin)  

