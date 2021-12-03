from django import forms
from django.db.models import fields
from . import models
from . models import Photo


class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body','group','tags','rating']

    def is_valid(self) -> bool:
        valid = super().is_valid()
        if not valid:
            return valid
        if '-' in self.cleaned_data['title']:
            return False
        else: return True
    

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']