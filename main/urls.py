from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('dashboard/<int:user_id>', views.dashboard, name='dashboard'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
    path('a/', views.a, name='a'),
    path('b/', views.b, name='b'),
]