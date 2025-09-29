from django import forms

from main.models import User, Task


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text']