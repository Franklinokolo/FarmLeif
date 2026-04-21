from django.contrib import admin
from .models import Transaction
# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'transaction_type', 'enterprise', 'created_at')
    search_fields = ('description', 'transaction_type')
    list_filter = ('transaction_type', 'created_at')