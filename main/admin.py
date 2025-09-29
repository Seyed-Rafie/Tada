from django.contrib import admin

from main.models import User, Task, UserDevice

# Register your models here.

admin.site.register(User)
admin.site.register(Task)
admin.site.register(UserDevice)