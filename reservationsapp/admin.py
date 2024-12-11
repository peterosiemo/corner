from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date', 'time', 'number_of_people', 'is_confirmed')
    list_filter = ('date', 'is_confirmed')
    search_fields = ('full_name', 'email', 'phone_number')
