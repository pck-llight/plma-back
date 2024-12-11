from django.db import models
from ninja import Schema


# Create your models here.
class Music(models.Model):
    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    singer = models.CharField(max_length=100)
    composer = models.CharField(max_length=100)
    star = models.BooleanField(default=False)

    def __str__(self):
        return self.title