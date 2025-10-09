from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('dashboard/<int:user_id>', views.dashboard, name='dashboard'),
    path('dashboard/<int:user_id>/delete_task/<int:task_id>', views.delete_task, name='delete_task'),
    path('dashboard/<int:user_id>/edit_task/<int:task_id>', views.edit_task, name='edit_task'),
    path('a/', views.a, name='a'),
    path('b/', views.b, name='b'),
]