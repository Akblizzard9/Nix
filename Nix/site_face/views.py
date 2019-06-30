from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import *
from .forms import *
from django.shortcuts import redirect, get_object_or_404
import datetime
from datetime import datetime, timedelta


# Create your views here.
class home(ListView):
        template_name = 'home.html'
        queryset = Resorts.objects.all()
        context_object_name = 'resorts'
        today = datetime.now().date()
        




class bookings(TemplateView):
    template_name = 'bookings.html'

    def get(self, request):
        allsnow = Reports.objects.all()
        context ={
            'allsnow' : allsnow
        }
        return render(request, self.template_name, context)

class gearup(TemplateView):
    template_name = 'gearup.html'

    def get(self, request):
        context = {

        }
        return render(request, self.template_name, context)

class resorts(ListView):
    template_name = 'resorts.html'
    queryset = Resorts.objects.all()
    context_object_name = 'resorts'

class resort_detail(DetailView):
    model = Resorts
    template_name = 'resort_detail.html'

