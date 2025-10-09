from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from main.forms import SignupForm, LoginForm, TaskForm
from main.models import User, Task, UserDevice

# Create your views here.

def home(request):
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')

    signup_form = SignupForm()
    return render(request, 'signup.html', {'form': signup_form})

def login(request):
    form = LoginForm()
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = User.objects.filter(username=username, password=password).first()
        if user:
            user_device = UserDevice.objects.filter(user=user, device=request.META.get('HTTP_USER_AGENT')).first()
            if user_device:
                user_device.save()
            else:
                UserDevice.objects.create(user=user, device=request.META.get('HTTP_USER_AGENT'), last_login=timezone.now())

            return redirect('dashboard', user_id=user.id)
        return render(request, 'login.html', {'form': form, "message": "your username or password is incorrect"}) ###

    else:
        return render(request, 'login.html', {'form': form, "message": "enter your username or password"})

def check_login(request, user_id):
    # check for valid user_id
    user = User.objects.filter(id=user_id).first()
    if not user:
        return False

    # check for device and last login
    user_device = UserDevice.objects.filter(user=user, device=request.META.get('HTTP_USER_AGENT')).first()
    if not user_device:
        return False
    if timezone.now() - user_device.last_login > timezone.timedelta(hours=1):
        return False

    # Update last login time
    user_device.last_login = timezone.now()
    user_device.save()
    return True

def dashboard(request, user_id):
    if not check_login(request, user_id):
        return redirect('login')
    user = User.objects.filter(id=user_id).first()
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.user = user
            task.save()
        return redirect('dashboard', user_id=user.id) ### change url
    task_form = TaskForm()
    return render(request, 'dashboard.html', {'user': user, 'task_form': task_form})

def delete_task(request, task_id, user_id):
    if not check_login(request, user_id):
        return redirect('login')
    user = User.objects.filter(id=user_id).first()
    if not user.tasks.filter(id=task_id).exists():
        return redirect('dashboard', user_id=user.id)
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('dashboard', user_id=task.user.id)

def edit_task(request, task_id, user_id):
    if not check_login(request, user_id):
        return redirect('login')
    user = User.objects.filter(id=user_id).first()
    if not user.tasks.filter(id=task_id).exists():
        return redirect('dashboard', user_id=user.id)
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect(dashboard, user_id=task.user.id)
    task = Task.objects.get(id=task_id)
    task_form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': task_form})




def a(request):
    redirect('b')
    return HttpResponse('a')
def b(request):
    return HttpResponse("<h1>hello world</h1>")