from django.contrib import admin
from .models import Rooms

class RoomAdmin(admin.ModelAdmin):
    list_display = ('block', 'floor', 'room_no')

admin.site.register(Rooms,RoomAdmin)
# Register your models here.
