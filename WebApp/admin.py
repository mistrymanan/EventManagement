from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm,UserCreationForm


class UserAdmin(UserAdmin):
    model = User
    add_form = UserCreationForm
    form = UserChangeForm


# Register your models here.
admin.register(User,UserAdmin)