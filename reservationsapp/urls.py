from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_reservation, name='create_reservation'),
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('<int:pk>/edit/', views.edit_reservation, name='edit_reservation'),
    path('<int:pk>/delete/', views.delete_reservation, name='delete_reservation'),
]
