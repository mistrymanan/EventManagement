from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import Event
from Database import models

class ManageEventView(ListView):
    model = Event
    context_object_name = 'events'
    queryset = Event.objects.all()
    template_name = 'manage_event.html'

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    # counts = {
    #     'cat_count': models.Catering.objects.count(),
    #     'venue_count': models.venue.objects.count(),
    #     'deco_count': models.Decoration.objects.count(),
    #     'sound_count': models.SoundSystem.objects.count()
    # }
    return render(request,'dashboard.html')

