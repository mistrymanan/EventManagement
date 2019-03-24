from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from Database.models import venue,SoundSystem, Profile,Decoration,Catering
from .forms import venueForm, SoundSystemForm
from accounts.models import User
from django.views import View

# Create your views here.

def index(request):
    user=Profile.objects.get(user=request.user)
    contex={'profile':user}
    return render(request,'StackHolder/index.html',contex)

class venuelistview(LoginRequiredMixin, ListView):
    model = venue
    template_name = 'StackHolder/venue_list.html'
    def get_queryset(self):
        return venue.objects.filter(user=self.request.user)


class venueDetailView(LoginRequiredMixin, DetailView):
    model = venue
    template_name = 'StackHolder/venue_detail.html'

    def get_queryset(self):
        print("from venue details")
        return venue.objects.all()

    def get_object(self, queryset=None):
        id = self.kwargs.get('pk')
        return get_object_or_404(venue, id=id)


class venueCreateView(LoginRequiredMixin, CreateView):
    model = venue
    form_class = venueForm
    template_name = 'StackHolder/venue_form_copy.html'
    success_url = ''

    # fields = ['name','ac','contact_no','Addressline','street','area','city','state','pincode','country','cost','capacity']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class venueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = venue
    form_class = venueForm
    template_name = 'StackHolder/venue_form_copy.html'
    success_url = ''

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    #    def get_object(self, queryset=None):
    #       return venue.objects.get(user=self.kwargs.get('pk'))

    def test_func(self):
        venue = self.get_object()
        if self.request.user == venue.user:
            return True
        return False


class SoundSystemListview(LoginRequiredMixin, ListView):
    model = SoundSystem
    template_name = 'StackHolder/SoundSystem_list.html'

    def get_queryset(self):
        return SoundSystem.objects.filter(user=self.request.user)


class SoundSystemDetailView(LoginRequiredMixin, DetailView):
    model = SoundSystem
    template_name = 'StackHolder/SoundSystem_detail.html'
    def get_queryset(self):
        print("calling systm")
        return SoundSystem.objects.all()

    def get_object(self, queryset=None):
        id = self.kwargs.get('pk')
        return get_object_or_404(SoundSystem, id=id)


class SoundSystemCreateView(LoginRequiredMixin, CreateView):
    model = SoundSystem
    form_class = SoundSystemForm
    template_name = 'StackHolder/SoundSystem_form.html'
    success_url = ''

    # fields = ['name','ac','contact_no','Addressline','street','area','city','state','pincode','country','cost','capacity']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SoundSystemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = SoundSystem
    form_class = SoundSystemForm
    template_name = 'StackHolder/SoundSystem_form.html'
    success_url = ''

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        SoundSystem = self.get_object()
        if self.request.user == SoundSystem.user:
            return True
        return False


class DecorationListview(LoginRequiredMixin, ListView):
    model = Decoration
    template_name = 'StackHolder/Decoration_list.html'

    def get_queryset(self):
        return Decoration.objects.filter(user=self.request.user)


class DecorationDetailView(LoginRequiredMixin, DetailView):
    model = Decoration
    template_name = 'StackHolder/Decoration_detail.html'
    def get_queryset(self):
        print("calling systm")
        return Decoration.objects.all()

    def get_object(self, queryset=None):
        id = self.kwargs.get('pk')
        return get_object_or_404(Decoration, id=id)


class DecorationCreateView(LoginRequiredMixin, CreateView):
    model = Decoration
    #form_class = SoundSystemForm
    template_name = 'StackHolder/Decoration_form.html'
    success_url = ''

    fields = ['name','contact_no','Addressline','street','area','city','state','pincode','country','cost']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DecorationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Decoration
    fields = ['name', 'contact_no', 'Addressline', 'street', 'area', 'city', 'state', 'pincode', 'country', 'cost']
    template_name = 'StackHolder/Decoration_form.html'
    success_url = ''

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Decoration= self.get_object()
        if self.request.user == Decoration.user:
            return True
        return False

class CateringListview(LoginRequiredMixin, ListView):
    model = Catering
    template_name = 'StackHolder/Catering_list.html'

    def get_queryset(self):
        return Catering.objects.filter(user=self.request.user)


class CateringDetailView(LoginRequiredMixin, DetailView):
    model = Catering
    template_name = 'StackHolder/Catering_detail.html'
    def get_queryset(self):
        print("calling systm")
        return Catering.objects.all()

    def get_object(self, queryset=None):
        id = self.kwargs.get('pk')
        return get_object_or_404(Catering, id=id)


class CateringCreateView(LoginRequiredMixin, CreateView):
    model = Catering
    #form_class = SoundSystemForm
    template_name = 'StackHolder/Catering_form.html'
    success_url = ''
    fields = ['name','foodtype','contact_no','Addressline','street','area','city','state','pincode','country','cost']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CateringUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Catering
    fields = ['name', 'contact_no','foodtype', 'Addressline', 'street', 'area', 'city', 'state', 'pincode', 'country', 'cost']
    template_name = 'StackHolder/Catering_form.html'
    success_url = ''

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Catering= self.get_object()
        if self.request.user == Catering.user:
            return True
        return False
