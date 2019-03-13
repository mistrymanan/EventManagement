from django.urls import path
from .views import ManageEventView
urlpatterns=[
    path('manageevent/',ManageEventView.as_view(), name ='dashboard')
]