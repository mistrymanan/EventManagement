from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm,UserCreationForm
from .models import venue,events,Address,invitation

# class UserAdmin(UserAdmin):
#     model = User
#     add_form = UserCreationForm
#     form = UserChangeForm
#

# Register your models here.
#admin.site.register(User,UserAdmin)
admin.site.register(venue)
admin.site.register(events)
admin.site.register(Address)
admin.site.register(invitation)

