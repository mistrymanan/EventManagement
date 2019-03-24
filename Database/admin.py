from django.contrib import admin
from .models import Catering,venue,MenuImage,invitation,Address,events,SoundSystem,Decoration
# Register your models here.

#admin.site.register(Catering)
admin.site.register(venue)
admin.site.register(SoundSystem)
admin.site.register(Decoration)
#admin.site.register(MenuImage)
#admin.site.register(invitation)
#admin.site.register(Address)
#admin.site.register(events)