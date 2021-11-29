from django.db.models import Q

from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import ArticleFilter
from django.template.defaultfilters import title
from .models import Article, Account
from . import forms


def index(request):    
    articles = Article.objects.all()
    print(articles[0].GROUP)
    articles = paginate(request, articles, modelPerPage=3   )
    return render(request, 'revapp/article_list.html',{'articles':articles})


def myArticles(request):
    account = Account.objects.select_related('user').filter(user=request.user).get()
    if account :
        myFilter = ArticleFilter(request.GET,queryset=Article.objects.filter(author = account))
        articles = myFilter.qs
    else:
        Account.objects.create(user=request.user)   
    return render(request, 'revapp/my_article.html', {'articles':articles, 'filter':myFilter})


def updateArticle(request, slug):
    if request.user != Article.objects.filter(slug=slug).first().author.user:
        return redirect('revapp:index')
    article = Article.objects.filter(slug=slug).first()
    form = forms.ArticleForm(request.POST,instance = article)
    if request.method == 'POST':
        if form.is_valid() and Article.objects.filter(title = request.POST['title']).count() == 0:
            article = form.save(commit=False).save()
            return redirect('revapp:myarticles')      
    else: form = forms.ArticleForm()
    return render(request,  'revapp/article_update.html', {'form':form, 'article':article})


def deleteArticle(request,slug):
    if request.user != Article.objects.filter(slug=slug).first().author.user:
        return redirect('revapp:index')
    Article.objects.filter(slug=slug).delete()
    return redirect ('revapp:myarticles')



def searchArticle(request):
    query =  request.GET.get('q')
    if query:
        articles = Article.objects.filter(Q(title__icontains=query)| Q(body__icontains=query))
    return render(request, 'revapp/article_list.html', {'articles':articles})
    

def paginate(request, someModel, modelPerPage=6):
    page = request.GET.get('page',1)
    paginator = Paginator(someModel, modelPerPage)
    try:
        someModel = paginator.page(page)
    except PageNotAnInteger:
        someModel = paginator.page(1)
    except EmptyPage:
        someModel = paginator.page(paginator.num_pages)
    return someModel