from django.contrib import admin
from .models import Cycle
# Register your models here.
@admin.register(Cycle)
class CycleAdmin(admin.ModelAdmin):
    list_display = ('name', 'enterprise', 'start_date', 'expected_duration', 'created_at')
    search_fields = ('name',)
    list_filter = ('start_date', 'expected_duration')