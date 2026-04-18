from django.db import models
from Enterprise.models import Enterprise

# Create your models here.
class Asset(models.Model):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    asset_type = models.CharField(max_length=100)

    purchase_value = models.DecimalField(max_digits=12, decimal_places=2)
    purchase_date = models.DateField()

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name