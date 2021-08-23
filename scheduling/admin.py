from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import  Notice, Person, Selected_person
   
class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       list_display=('first_Name','last_Name','age','gender','email_Id','phone_Num','person_room')
       search_fields=('first_Name','last_Name','age','gender','email_Id','phone_Num','person_room')
       list_filter = ('person_room',)
        #id, password, last_login, is_superuser, groups, user_permissions, email, first_name, last_name, is_staff, is_active, date_joined
       class Meta:
           model =Person
           exclude=('last_login','is_superuser','first_name')
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
admin.site.register(Notice)


