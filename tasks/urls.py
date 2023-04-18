from django.urls import path
from . import views

app_name='tasks'
urlpatterns = [
    path('<str:username>/income', views.income, name='income'),
    path('<str:username>/tasks/<int:id>/delete', views.deleteTask, name='deleteTask'),     
    path('<str:username>/tasks/<int:id>/update', views.updateTask, name='updateTask'), 
    path('<str:username>/tasks/new/<int:customerID>', views.createTask, name='newTask'),
    path('<str:username>/tasks/<int:id>', views.taskDetail, name='Taskdetail'),  
    path('<str:username>/tasks', views.taskList, name='alltasks'),         
]