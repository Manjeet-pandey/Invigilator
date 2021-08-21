from django.contrib import admin
from .models import Exam

class ExamAdmin(admin.ModelAdmin):
    list_display = ('date', 'level', 'manpower')

admin.site.register(Exam,ExamAdmin)