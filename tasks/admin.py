from django.contrib import admin
from .models import Task
from django.contrib import admin

admin.site.register(Task)

# class TaskAdmin(admin.ModelAdmin):
#     list_display = ['title', 'date_time_start', 'date_time_end', 'task_pay']
    
# admin.site.register(Task, TaskAdmin)