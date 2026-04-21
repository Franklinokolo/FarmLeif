from django.db import models

class Enterprise(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    farm_type = models.CharField(
        max_length=50,
        choices=[
            ("crop", "Crop"),
            ("livestock", "Livestock"),
            ("mixed", "Mixed"),
        ],
        default="mixed"
    )
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name