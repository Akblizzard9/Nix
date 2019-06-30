"""Nix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView
from site_face.views import *

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('site_face.urls')),
    path('home', (home.as_view()), name = 'home'),
    path('resorts', (resorts.as_view()), name = 'resorts'),
    path('resort/<slug>', resort_detail.as_view(template_name = 'resort_detail.html'), name='resort_detail'),
    path('booking', (bookings.as_view()), name = 'booking'),
    path('gear', (gearup.as_view()), name = 'gear' ),

]
