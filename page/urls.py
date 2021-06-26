from account.views import register
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teacher/', views.profile, name='profile'),
]