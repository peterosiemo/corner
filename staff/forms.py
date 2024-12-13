from django import forms
from .models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'role', 'bio', 'photo', 'twitter', 'facebook', 'instagram', 'linkedin']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter role or position'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a short bio', 'rows': 4}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Twitter profile URL'}),
            'facebook': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Facebook profile URL'}),
            'instagram': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Instagram profile URL'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter LinkedIn profile URL'}),
        }
