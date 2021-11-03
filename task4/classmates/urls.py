from django.urls import path
from . import views

app_name = 'classmates'

urlpatterns = [
    path('', views.index, name='home'),
    path('addbro', views.addBro,name='addbro'),
    path('addsis', views.addSis,name='addsis')
]