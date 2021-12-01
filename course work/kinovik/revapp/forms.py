from django import forms
from django.db.models import fields
from django.forms import widgets
from . import models


class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body','group','tags','images','rating']

    def is_valid(self) -> bool:
        valid = super().is_valid()
        if not valid:
            return valid
        if '-' in self.cleaned_data['title']:
            return False
        else: return True
    