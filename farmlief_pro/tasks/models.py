from django.db import models
import datetime
from cycles.models import Cycle
# Create your models here.


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

    status = [
        ('overdue', 'Overdue'),
        ('pending', 'Pending'),
        ('Completed','Completed')
    ]

    Cycle = models.ForeignKey(Cycle, on_delete= models.CASCADE)
    type = models.CharField(max_length=12, choices=TASK_CHOICES, default=VACCINATION)
    priority = models.CharField(max_length=6, choices=priority_choice, default='high')
    title = models.CharField(max_length= 100)
    due_date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False, default=datetime.time(9,0))
    status = models.CharField(max_length= 12, choices= status, default='pending', db_default='12:00')

    def __str__(self):
        return self.title
