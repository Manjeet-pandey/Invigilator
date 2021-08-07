
from django.urls import path

from . import views

urlpatterns = [
    path('', views.add_schedule, name='add_schedule'),
    path('view/', views.schedule, name='view_schedule'),
    # path("profile_id/", views.profile_id, name='profile_id'),
    # path("profile/<int:id>", views.profile, name='profile'),
]