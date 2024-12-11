from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('events/', views.events, name= 'events'),
    path('chefs/', views.chefs, name= 'chefs'),
    path('gallery/', views.gallery, name= 'gallery'),
    path('contact/', views.contact, name= 'contact'),
    path('book/', views.book, name= 'book'),

]