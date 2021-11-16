from django.shortcuts import render, redirect
from revapp.models import Article

def home(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html',{'articles':articles})