from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from .forms import UserChangeForm,UserCreationForm
from Database.models import events,Address,Profile
class modelProfile(admin.ModelAdmin):
    list_display=['id','user','image']


# Register your models here.
#admin.site.register(User,UserAdmin)
admin.site.register(Profile,modelProfile)
#admin.site.register(venue)
admin.site.register(events)
admin.site.register(Address)
#admin.site.register(invitation)


# Register your models here.
