from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect

from main.forms import LoginForm, TaskForm
from main.models import User, Task

# Create your views here.


def login(request):
    form = LoginForm()
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        # users = User.objects.filter(username=username, password=password)
        users = User.objects.all()
        # user = authenticate(request, username=username, password=password)
        for tuser in users:
            if tuser.username == username and tuser.password == password:
                user = tuser
                return redirect('dashboard', user_id=user.id)
                # return dashboard(request, user)

        return render(request, 'login.html', {'form': form, "message": "your username or password is incorrect"}) ###
    else:
        return render(request, 'login.html', {'form': form, "message": "enter your username or password"})

# def dashboard(request, user):
#     # if request.method == "POST":
#     #     data = request.POST
#     #     user.tasks.append(data.get('task'))
#     # redirect('dashboard') ### change url
#     # return render(request, 'dashboard.html', {'user': user})

def dashboard(request, user_id):
    user = User.objects.filter(id=user_id).first()
    if user is None: ###
        return redirect('login')

    if request.method == "POST":
        data = request.POST
        task = Task()
        task.user = user
        task.text = data.get('task')
        task.save()
# redirect('dashboard') ### change url
# return render(request, 'dashboard.html', {'user': user})
    task_form = TaskForm()
    return render(request, 'dashboard.html', {'user': user, 'task_form': task_form})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('dashboard', user_id=task.user.id)




def a(request):
    redirect('b')
    return HttpResponse('a')
def b(request):
    return HttpResponse("<h1>hello world</h1>")