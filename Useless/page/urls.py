from account.views import register
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path("profile_id/", views.profile_id, name='profile_id'),
    path("profile/<int:id>", views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),

]
