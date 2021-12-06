from django import forms
from . import models
from . models import Comment, Photo



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



class UpdateForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body','group', 'rating']
    

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']


class CommentForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Add a comment...'}))
    class Meta:
        model = Comment
        fields = ['body']


