from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from accounts.models import User
from customers.models import Customer
from .serializers import TaskSerializer
from rest_framework import status
from django.db.models import Sum, Count, Value, Avg
import pandas as pd
import decimal
import numpy as np


@api_view(['get'])
def income(request, username):
    user = User.objects.get(username=username)
    customers = Customer.objects.all()
    income = []
    for customer in customers:
        customerName = customer.customerName   
        weekly = Task.objects.filter(user=user, customer__customerName=customerName, isCompleted=True).values('week_of_year').annotate(
            total_hours=Sum('hours'), 
            regular_hours=Sum('regular_hours'),
            regular_pay=Sum('regular_pay'),
            daily_overtime=Sum('daily_overtime'),
            daily_overtime_pay=Sum('daily_overtime_pay'),
            evening_hours = Sum('evening_hours'),
            evening_pay = Sum('evening_pay'),
            weekend_hours = Sum('weekend_hours'),
            weekend_pay = Sum('weekend_pay'),
            stat_holiday = Sum('stat_holiday'),
            floater = Sum('floater'),
            ben_lieu = Sum('ben_lieu'),
            vacation_pay_out = Sum('vacation_pay_out'),
            pay=Sum('task_pay'),
            task_rate=Avg('task_rate')
            )
        for week in weekly:       
            weekly_overtime = week['total_hours'] - 40 if week['regular_hours'] >= 40 else week['daily_overtime']
            weekly_regular_hours = week['regular_hours'] if week['regular_hours'] < 40 else 40
            weekly_regular_pay = weekly_regular_hours*week['task_rate']
            weekly_overtime_pay = weekly_overtime*decimal.Decimal(1.5)*week['task_rate']
            ben_lieu = (weekly_regular_pay + weekly_overtime_pay + week['evening_pay'] + week['weekend_pay'])*decimal.Decimal(0.1)
            weekly_pay = (weekly_regular_pay + weekly_overtime_pay + week['evening_pay'] + week['weekend_pay'])*decimal.Decimal(1.1)
            week.update({
                'weekly_regular_hours': weekly_regular_hours,
                'weekly_regular_pay': weekly_regular_pay,
                'weekly_overtime': weekly_overtime,
                'weekly_overtime_pay': weekly_overtime_pay,
                'ben_lieu': ben_lieu,
                'weekly_pay': weekly_pay,
                })           
        
        total_regular_hours = []
        total_overtime = []
        total_pay = []
        for week in weekly:                 
            total_regular_hours.append(week['regular_hours'])  
            total_overtime.append(week['weekly_overtime'])  
            total_pay.append(week['weekly_pay']) 
            week.pop('regular_hours') if 'regular_hours' in week else None
            week.pop('regular_pay') if 'regular_pay' in week else None
            week.pop('daily_overtime') if 'daily_overtime' in week else None
            week.pop('daily_overtime_pay') if 'daily_overtime_pay' in week else None
            
        total_regular_hours = np.sum(total_regular_hours)      
        total_overtime = np.sum(total_overtime)
        total_pay = np.sum(total_pay)        
        income.append({
            customerName: {
                'weekly': sorted(weekly, key=lambda x: x['week_of_year']),
                'total_regular_hours': total_regular_hours,
                'total_overtime': total_overtime,
                'total_pay': total_pay                
            }
        })
                    
    return Response(income)
    # return Response(sorted(income, key=lambda x: x['customerName']))


@api_view(['PUT'])
def updateTask(request, username, id):
    try:
        task = Task.objects.get(id=id)        
        
    except Task.DoesNotExist:
        return Response({"error": "The task is not found"}, status=404)

    if request.method == "GET":
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'You do not have permision.'})


@api_view(['DELETE'])
def deleteTask(request, username, id):
    task = Task.objects.get(id=id)
    task.delete()

    return Response({'message': 'task was deleted'})


@api_view(['GET'])
def taskDetail(request, username, id):
    task = Task.objects.get(id=id)
    serializers = TaskSerializer(task, many=False)

    return Response(serializers.data)


@api_view(['GET'])
def taskList(request, username):
    tasks = Task.objects.all().order_by('-date_time_start')
    serializers = TaskSerializer(tasks, many=True)

    return Response(serializers.data)


@api_view(['POST'])
def createTask(request, username, customerID):
    if request.method != "POST":
        return Response({"error": "Task request required."})

    user = User.objects.get(username=username)
    title = request.data["title"]
    date_time_start = request.data['date_time_start']
    date_time_end = request.data['date_time_end']
    hours = request.data['hours']
    task_rate = request.data['task_rate']
    customer = Customer.objects.get(id=customerID)

    task = Task.objects.create(
        user = user,
        title = title,
        date_time_start = date_time_start,
        date_time_end = date_time_end,
        hours = hours,
        customer = customer,
        task_rate=task_rate,
    )
    task.save()

    return Response(TaskSerializer(task).data)
    # return Response({'start':date_time_start})
