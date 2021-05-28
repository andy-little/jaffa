from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('setups/', views.setups, name='setups'),
    path('equipment/', views.equipment, name='equipment'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
]
