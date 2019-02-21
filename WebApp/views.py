from django.shortcuts import render
# from django.template import RequestContext
from django.views import generic
from .forms import UserCreationForm
from django.urls import reverse_lazy
from .models import venue
# from django.http import HttpResponse
# Create your views here.
from django.views.generic import CreateView,UpdateView,DeleteView

def index(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'registration/login.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class VenueCreate(CreateView):
    model =venue
    fields = '__all__'

class VenueUpdate(UpdateView):
    model = venue
    fields = '__all__'
class VenueDelete(UpdateView):
    model = venue
    fields = '__all__'
