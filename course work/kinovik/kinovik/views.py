from django.shortcuts import render, redirect
from revapp.models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag



