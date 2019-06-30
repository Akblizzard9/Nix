from django import forms
from .models import *

class AvailableResortsForm(forms.Form):
    Available_Resorts = forms.ModelChoiceField(queryset=Resorts.objects.all())
