# Generated by Django 3.2.9 on 2021-11-27 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revapp', '0002_auto_20211127_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='articles_count',
        ),
    ]