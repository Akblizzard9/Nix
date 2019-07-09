from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import *
from .forms import *
from django.shortcuts import redirect, get_object_or_404
import datetime
from datetime import datetime, timedelta



# Create your views here.
class home(TemplateView):
        template_name = 'home.html'

        def get(self, request):
            today = datetime.now().date()
            top_ten_coldest = Reports.objects.filter(todays_date__gte = today).order_by('bottom_maxtemp')[:10]
            resorts = Resorts.objects.all()
            top_ten_snow = Reports.objects.filter(todays_date__gte = today).order_by('snowfall')[:10]

            context = {
                'top_ten_coldest' : top_ten_coldest,
                'resorts' : resorts,
                'top_ten_snow' : top_ten_snow,
               
            }

            return render(request, self.template_name, context)
        




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
    queryset = Resorts.objects.all().order_by('resort_name')
    context_object_name = 'reports'

class resort_detail(DetailView):
    model = Resorts.objects.all()
    template_name = 'resort_detail.html'

def get_data(request, *args, **kwargs):
    data = {
        'sales' : 100,
        'customers' : 10,
    }
    return JsonResponse(data)

    



