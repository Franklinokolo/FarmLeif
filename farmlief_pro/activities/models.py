from django.db import models
from enterprise.models import Enterprise
from cycles.models import Cycle

class Activity(models.Model):
    ACTIVITY_TYPE = [
        ("planting", "Planting"),
        ("feeding", "Feeding"),
        ("harvest", "Harvest"),
        ("treatment", "Treatment"),
        ("sale", "Sale"),
        ("other", "Other"),
    ]

    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, related_name="activities")

    title = models.CharField(max_length=255)
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_TYPE)

    description = models.TextField(blank=True)

    quantity = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=50, blank=True)

    cost = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    activity_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title