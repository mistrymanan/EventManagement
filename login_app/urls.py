from django.urls import path
from .views import loginPageView
from . import views
urlpatterns = [
    path('', loginPageView, name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]