from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import  Person
    
class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       class Meta:
           model =Person
        
admin.site.register(Person, BlogAdmin)  