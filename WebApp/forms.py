from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms


class UserCreationForm(UserCreationForm):
    gender_choices = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    gender = forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email',)


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')
