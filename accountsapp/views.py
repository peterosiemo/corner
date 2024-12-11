
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirect to profile page
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login1(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')  # Redirect to profile page
    else:
        form = AuthenticationForm()
    return render(request, 'login1.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})