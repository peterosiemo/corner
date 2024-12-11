from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations")
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    number_of_people = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()
    special_requests = models.TextField(blank=True, null=True)
    is_confirmed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation for {self.full_name} on {self.date} at {self.time}"
