from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='menu_photos/', blank=True, null=True)  # Add this field

    def __str__(self):
        return self.name
