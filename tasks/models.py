from django.db import models
from customers.models import Customer
from accounts.models import User
from datetime import date
from datetime import datetime
from django.utils import timezone
from pytz import timezone
import pytz
import datetime as dt
import decimal

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.TextField(null=True)
    date_time_start = models.DateTimeField(default=datetime.now())
    date_time_end = models.DateTimeField(default=datetime.now())  
    hours = models.DecimalField(null=True, max_digits=10, decimal_places=2)       
    task_rate = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)

    regular_hours = models.DecimalField(null=True, max_digits=10, decimal_places=2)  
    regular_pay = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)

    daily_overtime = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    daily_overtime_pay = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)

    stat_holiday = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    floater = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)

    evening_hours = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    evening_pay = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)

    weekend_hours = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    weekend_pay = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)

    vacation_pay_out = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    ben_lieu = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)

    task_pay = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    isCompleted = models.BooleanField(default=False) 
    
    week_of_year = models.IntegerField(null=True, blank=True)

    def __str__(self):       

        # get string of start and end time
        
        start_time = str(self.date_time_start.astimezone(pytz.timezone('America/New_York')))[11:19]        
        end_time = str(self.date_time_end.astimezone(pytz.timezone('America/New_York')))[11:19]

        start_date = str(self.date_time_start.astimezone(pytz.timezone('America/New_York')))[0:10]  
        workDate = datetime.strptime(start_date, "%Y-%m-%d")

        # get string of time point (15:00:00) at which  evening hours begins to be counted
        break_point = str(datetime.strptime(str(dt.time(15, 0, 0)), "%H:%M:%S"))[11:19]

        # convert start, end and break_time to time frame with format
        t1 = datetime.strptime(start_time, "%H:%M:%S")
        t2 = datetime.strptime(end_time, "%H:%M:%S")
        break_time = datetime.strptime(break_point, "%H:%M:%S")

        # calculate hours before and after the break point
        before_break_point = break_time - t1
        after_break_point = t2 - break_time

        # calculate hours and pay for regular, daily overtime, evening and weekend work
        if self.hours is not None and self.task_rate is not None:           
        
            self.regular_hours = self.hours if self.hours <=8 else 8
            self.regular_pay = (self.task_rate)*(self.regular_hours)    

            self.daily_overtime = (self.hours - 8) if self.hours > 8 else 0    
            self.daily_overtime_pay = self.daily_overtime*self.task_rate*decimal.Decimal(1.5)

            self.evening_hours = 0 if workDate.weekday() >= 5 else (
                int(str(after_break_point).split(':')[0]) 
                if after_break_point > before_break_point 
                and int(str(after_break_point).split(':')[0]) >= 4 
                else 0
                )
            self.evening_pay = self.evening_hours*decimal.Decimal(0.6) if workDate.weekday() < 5 else 0
            
            self.weekend_hours = self.hours if workDate.weekday() >= 5 else 0 
            self.weekend_pay = self.hours*decimal.Decimal(0.6) if workDate.weekday() >= 5 else 0 # check if the workday is weekend

            # Calculate all ben lieu from all work hours multiply 10%
            self.ben_lieu = (self.regular_pay + self.daily_overtime_pay + self.evening_pay + self.weekend_pay )*decimal.Decimal(0.1)

            # Calculate all earning from the task
            self.task_pay = self.regular_pay + self.daily_overtime_pay + self.evening_pay + self.weekend_pay + self.ben_lieu

            super(Task, self).save()

            return self.title
