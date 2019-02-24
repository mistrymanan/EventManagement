from django.urls import path,include
from . import views
urlpatterns=[
    #path('', views.index, name='index')
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', views.index),
    path('logintemp/',views.login),
    path('profile/new/',views.ProfileCreateView.as_view(),name='profile-create'),
    path('profile/update/',views.ProfileUpdateView.as_view(),name='profile-update'),
    path('profile/',views.profile,name='profile'),
    path('profile/address/new/',views.AddressCreateView.as_view(),name='address-create'),
    path('profile/address/update/',views.AddressUpdateView.as_view(),name='address-update'),

]