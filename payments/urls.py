
from django.urls import path
from . import views

urlpatterns = [
    path('initiate/', views.initiate_payment, name='initiate_payment'),
    path('confirmation/', views.payment_confirmation, name='payment_confirmation'),
]
