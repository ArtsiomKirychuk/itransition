# Generated by Django 3.2.9 on 2021-12-04 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('revapp', '0006_auto_20211203_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='views',
        ),
        migrations.CreateModel(
            name='Views',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.IntegerField(default=0)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='revapp.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='revapp.account')),
            ],
        ),
    ]
