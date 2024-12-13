from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone_number', 'amount', 'transaction_id', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('transaction_id', 'user__username', 'phone_number')
