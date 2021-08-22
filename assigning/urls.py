from django.urls import path
from .import views

urlpatterns =[
    path('selection/',views.selection,name='selection'),
]