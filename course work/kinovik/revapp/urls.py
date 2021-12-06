from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'revapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.searchArticle, name='search'),
    path('group/', views.groupArticle, name='group'),
    path('create/', views.createArticle, name='create'),
    path('rate-article/', views.rateArticle, name='ratearticle'),
    path('my-articles/', views.myArticles, name='myarticles'),
    path('tag/<slug:slug>/', views.tagged, name='tagged'),
    path('<slug:slug>/like', views.likeUnlikeArticle, name='likeunlike'),
    path('<slug:slug>/detail', views.detailArticle, name='detail'),
    path('<slug:slug>/album', views.otherImages, name='otherimages'),
    path('<slug:slug>/update', views.updateArticle, name="update"),
    path('<slug:slug>/delete', views.deleteArticle, name='delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
