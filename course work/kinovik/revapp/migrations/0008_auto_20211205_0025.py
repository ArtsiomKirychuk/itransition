# Generated by Django 3.2.9 on 2021-12-05 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revapp', '0007_auto_20211204_0100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_created']},
        ),
        migrations.RemoveField(
            model_name='views',
            name='view',
        ),
    ]
