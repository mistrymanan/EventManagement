from django.shortcuts import render
from django.views.generic import ListView
from .models import Event

class ManageEventView(ListView):
    model = Event
    context_object_name = 'events'
    queryset = Event.objects.all()
    template_name = 'manage_event.html'
