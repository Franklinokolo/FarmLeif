from django.db import models
from Enterprise.models import Enterprise
from Cycles.models import Cycle
from Activities.models import Activity
# Create your models here.
class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ("income", "Income"),
        ("expense", "Expense"),
    ]

    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycle, on_delete=models.SET_NULL, null=True, blank=True)

    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, null=True, blank=True)

    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE)

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True)

    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"