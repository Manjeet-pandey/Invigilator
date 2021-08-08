
from django.urls import path

from . import views
from page import views as page_view

urlpatterns = [
    path('', views.add_schedule, name='add_schedule'),
    path('view/', views.schedule, name='view_schedule'),
    path('update/<int:id>', views.update_schedule, name='update_schedule'),
    path('delete/<int:id>', views.del_schedule, name='delete_schedule'),
    # path('home/', page_view, name='home'),
    # path("profile_id/", views.profile_id, name='profile_id'),
    # path("profile/<int:id>", views.profile, name='profile'),
]