
from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('', include('classmates.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
