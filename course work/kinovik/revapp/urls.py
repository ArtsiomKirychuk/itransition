
from django.urls import path
from . import views


app_name = 'revapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.searchArticle, name='search'),
    path('my-articles/', views.myArticles, name='myarticles'),
    path('<slug:slug>/update', views.updateArticle, name="update"),
    path('<slug:slug>/delete', views.deleteArticle, name='delete'),
]
