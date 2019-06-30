from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'home.html'), name = 'home'),
    path('/resorts', TemplateView.as_view(template_name = 'resorts.html'), name = 'resorts'),
    path('/resorts/<slug>', TemplateView.as_view(template_name = 'resort_detail.html'), name='resort_detail'),
    path('/bookings', TemplateView.as_view(template_name = 'bookings.html'), name = 'bookings'),
    path('/gearup', TemplateView.as_view(template_name = 'gearup.html'), name = 'gearup'),

]