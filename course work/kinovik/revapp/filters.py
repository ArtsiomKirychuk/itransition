from django.db.models import fields
from django.db.models.enums import Choices
import django_filters

from .models import *

class ArticleFilter(django_filters.FilterSet):
    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )
    ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Article
        fields = ['group']

    def filter_by_order(self, queryset, name, value):
        expression = 'date_created' if value =='ascending' else '-date_created'
        return queryset.order_by(expression)