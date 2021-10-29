from django.db import models

# Create your models here.

class Contents(models.Model):
    objects = None
    title = models.CharField(max_length=20)
    word_text = models.CharField(max_length=140)
    date_time = models.DateTimeField('投稿日')
