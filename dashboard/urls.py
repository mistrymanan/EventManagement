from django.urls import path
from .views import ManageEventView, dashboard
urlpatterns=[
    path('manageevent/',ManageEventView.as_view(), name ='manageevent'),
    path('', dashboard, name ='dashboard')
]