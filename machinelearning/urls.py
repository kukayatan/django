
from django.contrib import admin
from django.urls import path,include
from .views import ml_view


urlpatterns = [
    path('', ml_view, name='ml_home'),
    
]