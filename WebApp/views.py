from django.shortcuts import render
from django.template import RequestContext
from django.views import generic
from .forms import UserCreationForm
from django.urls import reverse_lazy
from .models import User
from django.http import HttpResponse
# Create your views here.

def index(request):

    return render(request,'home.html')
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'