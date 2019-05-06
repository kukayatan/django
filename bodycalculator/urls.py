from django.contrib import admin
from django.urls import path
from .views import bodycalc_view, bmi, whr


urlpatterns = [
    path('', bodycalc_view, name='bodycalculator'),
    path('bmi/', bmi, name='bmi'),
    path('whr/', whr, name='whr'),

]