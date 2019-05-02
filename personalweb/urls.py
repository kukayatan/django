"""personalweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from portfolio.views import home_view,about
from wordcounter.views import words_putin, export_view_gener
from generator.views import gener_putin,export_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('about/', about, name='about'),
    path('words/', words_putin, name='words'),
    path('exportgener/', export_view_gener, name='exportgener'),
    path('generator/', gener_putin, name='generator'),
    path('export/', export_view, name='export'),
]
