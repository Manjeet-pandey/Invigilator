from django.contrib import admin

from .models import Teacher, Staff, Student

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Staff)