from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

from cloudinary.models import CloudinaryField



class Article(models.Model):
    GROUP = [
        ('Movie', 'Movie'),
        ('Games', 'Games'),
        ('Books', 'Books')
    ]
    title = models.CharField(max_length=200, unique=True, null=True)
    group = models.CharField(max_length=100, choices=GROUP, null=True)
    body = models.TextField()
    tags = TaggableManager()
    images = CloudinaryField('image')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    fans = models.ManyToManyField(User, related_name='artiles')
