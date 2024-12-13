from django import forms
from .models import Order

class OrderFilterForm(forms.Form):
    STATUS_CHOICES = [
        ('', 'All'),
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('CANCELED', 'Canceled'),
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, label="Order Status")
