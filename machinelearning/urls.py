
from django.contrib import admin
from django.urls import path,include
from .views import ml_view, ml_linreg,ml_svc,ml_nlp


urlpatterns = [
    path('', ml_view, name='ml_home'),
    path('ml_linreg/', ml_linreg, name='ml_linreg'),
    path('ml_svc/', ml_svc, name='ml_svc'),
    path('ml_nlp/', ml_nlp, name='ml_nlp'),
]