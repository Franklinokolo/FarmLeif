from django.contrib import admin
from .models import Activity
# Register your models here.

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'enterprise', 'activity_type', 'activity_date', 'created_at')
    search_fields = ('title', 'activity_type')
    list_filter = ('activity_type',)
