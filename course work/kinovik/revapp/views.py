from django.db import connection
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.sql.query import RawQuery
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import ArticleFilter
from .models import Article, Account, Comment, Photo, Like, Rating, Views
from taggit.models import Tag
from django.http import JsonResponse
from . import forms


def index(request):  
    checkAccount(request)
    articles = Article.objects.all()
    articles = sorted(articles, key=lambda x: x.numLikes(), reverse=True)
    articles = paginate(request, articles, modelPerPage=6)
    return render(request, 'revapp/article_list.html',{'articles':articles})

@login_required(login_url='/accounts/login')
def myArticles(request):
    account = Account.objects.select_related('user').filter(user=request.user).get()
    if account :
        myFilter = ArticleFilter(request.GET,queryset=Article.objects.filter(author = account))
        articles = myFilter.qs
    else:
        Account.objects.create(user=request.user)
    return render(request, 'revapp/my_article.html', {'articles':articles, 'filter':myFilter})

def detailArticle(request,slug):
    article = Article.objects.filter(slug=slug).get()
    print(article.calculateRating())
    if request.method =='POST':
        c_form = forms.CommentForm(request.POST)
        if c_form.is_valid():
            comment = c_form.save(commit=False)
            comment.user = Account.objects.filter(user = request.user).get()
            comment.article = article
            comment.save()
            c_form = forms.CommentForm()
    else:
        c_form = forms.CommentForm()
    if request.user.is_authenticated:
        account = Account.objects.get(user=request.user)
        views, created = Views.objects.get_or_create(user=account, article_id=article.id)
        if created:
            views.save()  
    else:
        account={}
    return render(request, 'revapp/article_detail.html', {'article':article,'account':account,'c_form':c_form})

login_required(login_url='/accounts/login')
def rateArticle(request):
    if request.method=='POST':
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        article = Article.objects.get(id=el_id)
        account = Account.objects.get(user = request.user)
        rat, created=Rating.objects.get_or_create(article=article, user = account)
        rat.score = val
        rat.save()
        return JsonResponse({'success':'true', 'score':val}, safe=False)
    return JsonResponse({'success':'false'})

@login_required(login_url='/accounts/login')
def createArticle(request):
    if request.method=='POST':
        images =  request.FILES.getlist('images')
        form = forms.ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = Account.objects.filter(user_id=request.user.id).first()
            article.save()
            addImages(article,images)
            form.save_m2m()
            return redirect('revapp:myarticles')
    else:
        form = forms.ArticleForm()
    return render(request, 'revapp/article_create.html',{'form':form})

@login_required(login_url='/accounts/login')
def updateArticle(request, slug):
    if request.user != Article.objects.filter(slug=slug).first().author.user:
        return redirect('revapp:index')
    article = Article.objects.filter(slug=slug).get()
    form = forms.UpdateForm(request.POST, instance=article)
    if request.method == 'POST':
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            form.save_m2m()
            return redirect('revapp:myarticles')      
    else:
         form = forms.ArticleForm(instance=article)
    return render(request,  'revapp/article_update.html', {'form':form, 'article':article})

def otherImages(request, slug):
    photoObj = Article.objects.filter(slug=slug).get().images.all()
    images = []
    for obj in photoObj:
        images.append(obj.image)
    return render (request, 'revapp/article_album.html', {'images':images,'slug':slug})

@login_required(login_url='/accounts/login')
def deleteArticle(request,slug):
    if request.user != Article.objects.filter(slug=slug).first().author.user:
        return redirect('revapp:index')
    Article.objects.filter(slug=slug).delete()
    return redirect ('revapp:myarticles')

@login_required(login_url='/accounts/login')
def likeUnlikeArticle(request, slug):
    if request.method =='POST':
        article = Article.objects.filter(slug=slug).get()
        account = Account.objects.filter(user=request.user).get()
        article_id = request.POST.get('article_id')
        if account in article.fans.all():
            article.fans.remove(account)
        else:
            article.fans.add(account)
        like, created = Like.objects.get_or_create(user=account, article_id=article_id)
        if not created:
            like.value = 'Unlike' if like.value=='Like' else 'Like'
        else:
            like.value='Like'
        like.save()
        article.save()
    return redirect('revapp:detail', slug =slug)

def searchArticle(request):
    query =  request.GET.get('q')
    articles = set()
    if query:     
        articles.update(Article.objects.filter(Q(title__icontains=query)| Q(body__icontains=query)))    
        print(articles)
        comments = Comment.objects.filter(Q(body__icontains=query))
        artcomm = [comment.article for comment in comments]
        articles.update(artcomm)

    return render(request, 'revapp/article_list.html', {'articles':articles})

def groupArticle(request):
    group = request.GET['group']
    articles = []
    for item in Article.GROUP:
        if group in item:
            articles = Article.objects.filter(group=group).all()
            return render( request, 'revapp/article_list.html', {'articles': articles})
    return redirect('revapp:index')
    
def tagged(request,slug):
    tag = get_object_or_404(Tag, slug=slug)
    articles =  Article.objects.filter(tags=tag)
    return render(request, 'revapp/article_list.html', {'articles':articles,'tag':tag})

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

def checkAccount(request):
    if request.user.is_authenticated:
        account,created = Account.objects.get_or_create(user=request.user)

def addImages(article,images):
    for image in images:
        Photo.objects.create(image=image, article =article)