from django.contrib import admin
from .models import Farmer, Enterprise

# Register your models here.
@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'address', 'role')
    search_fields = ('username', 'email', 'phone_number')
    list_filter = ('role',)

@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'farmer', 'location', 'farm_type', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'location')
    list_filter = ('farm_type', 'is_active')