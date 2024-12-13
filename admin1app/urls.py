from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register1/', views.register1, name='register1'),
    path('login3/', views.login3, name='login3'),
    path('admin2/', views.admin2, name='admin2'),
    path('logout/', LogoutView.as_view(next_page='index/'), name='logout'),
    path('', views.home, name='home'),  # Home page
]
