from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from  .models import Event

# Create your views here.

class EventList(ListView):
    model = Event
    
