from django.db import models
from enterprise.models import Enterprise

# Create your models here.
class Cycle(models.Model):
    CYCLE_TYPE = [
        ("crop", "Crop"),
        ("livestock", "Livestock"),
    ]

    STATUS = [
        ("active", "Active"),
        ("completed", "Completed"),
        ("archived", "Archived"),
    ]

    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, related_name="cycles")

    name = models.CharField(max_length=255)
    cycle_type = models.CharField(max_length=20, choices=CYCLE_TYPE)

    start_date = models.DateField()
    expected_duration = models.IntegerField(null=True, blank=True)  # days

    status = models.CharField(max_length=20, choices=STATUS, default="active")

    # Crop-specific
    crop_type = models.CharField(max_length=100, blank=True)
    season = models.CharField(max_length=100, blank=True)

    # Livestock-specific
    livestock_type = models.CharField(max_length=100, blank=True)
    breed = models.CharField(max_length=100, blank=True)
    initial_count = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name