from django.db import models
from django.utils import timezone
import datetime
from cycles.models import Cycle
# Create your models here.


class TaskStatusCheck(models.QuerySet):
    def pending(self):
        return self.filter(is_complete = False, due_date__gte = timezone.localdate())
        
    def overdue(self):
        return self.filter(is_complete = False, due_date__lt = timezone.localdate())



class Task(models.Model):

    FEEDING = 'FEED'
    VACCINATION = 'VACCINE'
    CLEANING = 'CLEANING'
    OTHERS = 'OTHERS'

    TASK_CHOICES = {
        FEEDING: "Feeding",
        VACCINATION: "Vaccination",
        CLEANING: "Cleaning",
        OTHERS: "Others"
    }

    priority_choice = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low')
    ]



    Cycle = models.ForeignKey(Cycle, on_delete= models.CASCADE, related_name='cycle')
    type = models.CharField(max_length=12, choices=TASK_CHOICES, default=VACCINATION)
    priority = models.CharField(max_length=6, choices=priority_choice, default='high')
    title = models.CharField(max_length= 100)
    description = models.TextField(default= "no description for this task")
    due_date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False, default=datetime.time(9,0))
    is_complete = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(default=timezone.now)


    objects = TaskStatusCheck.as_manager()
    
    @property
    def status_label(self):
        if self.is_complete:
            return 'Completed'
            
        current_date = timezone.localdate()
        current_time = timezone.localtime(timezone.now()).time()

        # Task date is in the absolute past
        if self.due_date < current_date:
            return 'Overdue'
            
        # Task date is TODAY, but the specific time has passed
        if self.due_date == current_date and self.time < current_time:
            return 'Overdue'
            
        return 'Pending'
    def __str__(self):
        return self.title
    
    