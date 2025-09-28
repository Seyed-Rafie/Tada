from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('a/', views.a, name='a'),
    path('b/', views.b, name='b'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
]