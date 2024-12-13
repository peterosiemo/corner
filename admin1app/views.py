# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm

def register1(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login3')
    else:
        form = RegistrationForm()
    return render(request, 'register1.html', {'form': form})

def login3(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser:  # Check if the user is an admin
                return redirect('admin2')  # Admin page
            else:
                return redirect('admin2')  # Redirect non-admin users to home page
    else:
        form = LoginForm()
    return render(request, 'login1.html', {'form': form})

@login_required
def admin2(request):
    return render(request, 'admin2.html')

def home(request):
    return render(request, 'index.html')  # A simple home page for non-admin users

