
from django.urls import path,include
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static
from .views import venuelistview,SoundSystemListview

from . import views
urlpatterns=[
    #path('', views.index, name='index')
    #path('', , name=''),
    path('',views.index ,name='seller'),
    path('venue/',venuelistview.as_view(),name='seller-venue-list'),
    path('venue/<int:pk>',views.venueDetailView.as_view(),name='venue-detail'),
    path('venue/create',views.venueCreateView.as_view(),name='venue-create'),
    path('venue/<int:pk>/update',views.venueUpdateView.as_view(),name='venue-update'),
    path('SoundSystem/',views.SoundSystemListview.as_view(),name='seller-SoundSystem-list'),
    path('SoundSystem/<int:pk>',views.SoundSystemDetailView.as_view(),name='seller-SoundSystem-detail'),
    path('SoundSystem/create', views.SoundSystemCreateView.as_view(), name='seller-SoundSystem-create'),
    path('SoundSystem/<int:pk>/update', views.SoundSystemUpdateView.as_view(), name='seller-SoundSystem-update'),
    path('Decoration/',views.DecorationListview.as_view(),name='seller-Decoration-list'),
    path('Decoration/<int:pk>',views.DecorationDetailView.as_view(),name='seller-Decoration-detail'),
    path('Decoration/create', views.DecorationCreateView.as_view(), name='seller-Decoration-create'),
    path('Decoration/<int:pk>/update', views.DecorationUpdateView.as_view(), name='seller-Decoration-update'),
    path('Catering/',views.CateringListview.as_view(),name='seller-Catering-list'),
    path('Catering/<int:pk>',views.CateringDetailView.as_view(),name='seller-Catering-detail'),
    path('Catering/create', views.CateringCreateView.as_view(), name='seller-Catering-create'),
    path('Catering/<int:pk>/update', views.CateringUpdateView.as_view(), name='seller-Catering-update'),


]