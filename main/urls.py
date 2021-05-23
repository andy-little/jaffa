from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('setups/', views.setups, name='setups'),
    
]
