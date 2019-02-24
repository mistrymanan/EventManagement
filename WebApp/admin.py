from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm,UserCreationForm
from .models import venue,events,Address,invitation,Profile

class modelProfile(admin.ModelAdmin):
    list_display=['id','user','image']


# Register your models here.
#admin.site.register(User,UserAdmin)
admin.site.register(Profile,modelProfile)
admin.site.register(venue)
admin.site.register(events)
admin.site.register(Address)
admin.site.register(invitation)

