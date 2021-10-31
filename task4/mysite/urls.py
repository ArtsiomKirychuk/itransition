
from django.contrib import admin
from django.urls import include, path
from .views import Home 


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', Home.as_view(), name='home'),
    path('classmates/', include('classmates.urls')),
    path('admin/', admin.site.urls),
]
