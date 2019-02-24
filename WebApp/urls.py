from django.urls import path,include
from . import views
urlpatterns=[
    path('profile/new/',views.ProfileCreateView.as_view(),name='profile-create'),
    path('profile/update/',views.ProfileUpdateView.as_view(),name='profile-update'),
    path('profile/',views.profile,name='profile'),
    path('profile/address/new/',views.AddressCreateView.as_view(),name='address-create'),
    path('profile/address/update/',views.AddressUpdateView.as_view(),name='address-update'),

]