from django import forms
from Database.models import venue,SoundSystem
class venueForm(forms.ModelForm):
    class Meta:
        model=venue
        fields = ['name', 'ac', 'contact_no', 'Addressline', 'street', 'area', 'city', 'state', 'pincode', 'country',
                  'cost', 'capacity','image']
        user =forms.CharField(max_length=100,widget=forms.HiddenInput())
        capacity = forms.CharField(max_length=150)
        ac_choice = (('ac', "A/C"), ('non-ac', 'Non A/c'))
        image=forms.ImageField()
        ac = forms.ChoiceField(choices=ac_choice,widget=forms.Select())
        contact_no = forms.CharField(max_length=150)
        cost = forms.CharField(max_length=150)
        #is_active = forms.BooleanField(default=True)
        name = forms.CharField(max_length=150)
        Addressline = forms.CharField(max_length=150)
        street = forms.CharField(max_length=150)
        area = forms.CharField(max_length=150)
        city = forms.CharField(max_length=150)
        state = forms.CharField(max_length=150)
        pincode = forms.CharField(max_length=150)
        country = forms.CharField(max_length=150)

class SoundSystemForm(forms.ModelForm):
    class Meta:
        model=SoundSystem
        fields = ['name', 'contact_no', 'Addressline', 'street', 'area', 'city', 'state', 'pincode', 'country',
                  'cost']
        user =forms.CharField(max_length=100,widget=forms.HiddenInput())
        contact_no = forms.CharField(max_length=150)
        cost = forms.CharField(max_length=150)
        #is_active = forms.BooleanField(default=True)
        name = forms.CharField(max_length=150)
        Addressline = forms.CharField(max_length=150)
        street = forms.CharField(max_length=150)
        area = forms.CharField(max_length=150)
        city = forms.CharField(max_length=150)
        state = forms.CharField(max_length=150)
        pincode = forms.CharField(max_length=150)
        country = forms.CharField(max_length=150)