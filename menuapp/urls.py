from django.urls import path
from . import views

urlpatterns = [
    path('menu1', views.menu1, name='menu1'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_menu_item/', views.add_menu_item, name='add_menu_item'),
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('adminmenuc/', views.adminmenuc, name='adminmenuc'),
]
