# Generated by Django 3.2.9 on 2021-11-15 22:27

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True, unique=True)),
                ('group', models.CharField(choices=[('Movie', 'Movie'), ('Games', 'Games'), ('Books', 'Books')], max_length=100, null=True)),
                ('body', models.TextField()),
                ('images', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('likes', models.IntegerField(default=0)),
                ('fans', models.ManyToManyField(related_name='liked_articles', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
