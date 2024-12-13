from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login1/', views.login1, name='login1'),
    path('profile/', views.profile, name='edit_profile'),
]
