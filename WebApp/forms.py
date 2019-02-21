from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import venue
from django.forms import ModelForm

# class UserCreationForm(UserCreationForm):
#     gender_choices = (
#         ('m', 'Male'),
#         ('f', 'Female'),
#     )
#     gender = forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
#     class Meta(UserCreationForm):
#         model = User
#         fields = ('username', 'email',)
#
#
# class UserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = User
#         fields = ('username', 'email')

class venueForm(ModelForm):

    class Meta:
        model=venue
        fields=['__all__']