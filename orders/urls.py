from django.urls import path
from . import views

urlpatterns = [
    path('place/', views.place_order, name='place_order'),
    path('track/', views.track_orders, name='track_orders'),
    path('orders/', views.order_list, name='order_list'),
    
]
