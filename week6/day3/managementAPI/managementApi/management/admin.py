from django.contrib import admin
from .models import Department, Project, Task, Employee

# Register your models here.
admin.site.register(Department)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Employee)
