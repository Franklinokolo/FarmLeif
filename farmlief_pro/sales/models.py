from django.db import models
from enterprise.models import Enterprise
from cycles.models import Cycle

# Create your models here.
class Sale(models.Model):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, related_name="sales")

    product_name = models.CharField(max_length=255)
    quantity = models.FloatField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    total_amount = models.DecimalField(max_digits=12, decimal_places=2)

    sale_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name