from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=100, help_text="Full name of the staff member")
    role = models.CharField(max_length=100, help_text="Role or position of the staff member")
    bio = models.TextField(help_text="A short bio of the staff member")
    photo = models.ImageField(upload_to='staff_photos/', help_text="Upload a photo of the staff member")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter profile link")
    facebook = models.URLField(blank=True, null=True, help_text="Facebook profile link")
    instagram = models.URLField(blank=True, null=True, help_text="Instagram profile link")
    linkedin = models.URLField(blank=True, null=True, help_text="LinkedIn profile link")

    def __str__(self):
        return self.name

