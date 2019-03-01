
from django.urls import path,include
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns=[
    #path('', views.index, name='index')
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('', views.index,name='index'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate,name='activate')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)