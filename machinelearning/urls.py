
from django.contrib import admin
from django.urls import path,include
from .views import ml_view, ml_linreg


urlpatterns = [
    path('', ml_view, name='ml_home'),
    path('ml_linreg/', ml_linreg, name='ml_linreg'),
]