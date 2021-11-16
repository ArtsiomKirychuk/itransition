# Generated by Django 3.2.9 on 2021-11-15 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revapp', '0003_article_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=-1),
        ),
    ]