from django.db import models
from django.conf import settings

# farmers account using the abstract user model the farmers will be able to login and manage their enterprise
from django.contrib.auth.models import AbstractUser


class Farmer(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    role = models.CharField(
        max_length=20,
        choices=[
            ("farmer", "Farmer"),
            ("manager", "Manager"),
            ("admin", "Admin"),
        ],
        default="farmer"
    )
    def __str__(self):
        return self.username
        



class Enterprise(models.Model):
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enterprises')
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
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
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


