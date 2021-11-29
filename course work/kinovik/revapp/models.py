from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify as d_slug
from cloudinary.models import CloudinaryField

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}

def slugify(s):
    return d_slug(''.join(alphabet.get(w, w) for w in s.lower()))


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    

class Article(models.Model):
    GROUP = [
        ('Movie', 'Movie'),
        ('Games', 'Games'),
        ('Books', 'Books')
    ]
    SCALE =[(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (10,10)]
    title = models.CharField(max_length=200, unique=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    group = models.CharField(max_length=100, choices=GROUP, null = True)
    body = models.TextField()
    tags = TaggableManager()
    images = CloudinaryField('image', blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    date_updated = models.DateTimeField(auto_now=True,null=True)
    fans = models.ManyToManyField(User, related_name='liked_articles', blank=True)
    likes = models.IntegerField(default=0)
    rating = models.IntegerField(default=-1, choices=SCALE)
    views = models.BigIntegerField(default=0)
    author = models.ForeignKey(Account, on_delete=models.CASCADE, default=None)
    

    def __str__(self):
        return self.title
    
    def snippet(self):
        if self.body != '':
            return self.body[:30] + '...'
        else:
            return '[]'    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)



