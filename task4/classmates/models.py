from django.db import models


class Message(models.Model):
    title = models.CharField(default='', max_length=150)
    username = models.CharField(default='', max_length=150)
    date = models.DateTimeField(auto_now=True)
    bro = models.BigIntegerField(default=0)
    sis = models.BigIntegerField(default=0)

    def __str__(self) -> str:
        return  f'{self.bro} Bro {self.sis} Sis'