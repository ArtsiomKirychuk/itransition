from django.db.models import fields
import django_filters

from .models import *

class ArticleFilter(django_filters.FilterSet):
    class Meta:
        model = Article
        fields = ['group']