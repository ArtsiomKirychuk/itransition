from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify as d_slug
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}

def slugify(s):
    return d_slug(''.join(alphabet.get(w, w) for w in s.lower()))


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.user.username)
    
    def get_likes_given(self):
        likes = self.likes.all()
        totalLikes = 0
        for item in likes:
            if item.value == "Like":
                totalLikes += 1
        return totalLikes

    def get_likes_recieved(self):
        articles = self.articles.all()
        total =  0
        for item in articles:
            total += item.fans.all().count()
        return total 


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
    body = RichTextField(blank = True)   
    tags = TaggableManager()
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    date_updated = models.DateTimeField(auto_now=True,null=True)
    fans = models.ManyToManyField(Account, related_name='liked', blank=True)
    rating = models.IntegerField(default=-1, choices=SCALE)
    author = models.ForeignKey(Account, on_delete=models.CASCADE, default=None, related_name='articles')

    class Meta:
        ordering = ['-date_created']    

    def __str__(self):
        return self.title
    
    def snippet(self):
        if self.body != '':
            return self.body[:30]
        else:
            return '[]'    
    
    def numLikes(self):
        return self.fans.all().count()

    def numViews(self):
        return self.views.all().count()

    def numComments(self):
        return self.comments.all().count()

    def numRat(self):
        return self.stars.all().count()
    
    def calculateRating(self):
        stars = self.stars.all()
        numStars = self.numRat()
        average = [x.score/numStars for x in stars]
        sum = 0
        for el in average: sum += el
        return sum

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)


class Views(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='views')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='views')

    def __str__(self):
        return f'{self.article.title}-{self.user.user.username}'
    


class Comment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    date_updated = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return str(self.pk)
    

class Like(models.Model):
    LIKE_CHOICES = [
        ('Like','Like'),
        ('Unlike', 'Unlike'),
    ]
    
    user =models.ForeignKey(Account, on_delete=models.CASCADE, related_name='likes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
    value =  models.CharField(choices=LIKE_CHOICES, max_length=10)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    date_updated = models.DateTimeField(auto_now=True,null=True)

    def __str__ (self):
        return f"{self.user}-{self.article}-{self.value}"



class Photo(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')


class Rating(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='stars')
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='stars')
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])

    def __str__(self):
        return f'{self.article.title}-{self.user.user.username}-{self.score}'
    