
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('i18n/', include('django.conf.urls.i18n')),
    
]

urlpatterns += i18n_patterns(
    path('accounts/',include('allauth.urls')),
    path('', include('revapp.urls')),
)
