# -*- encoding: utf-8; -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    rating = models.IntegerField()
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    # http://stackoverflow.com/a/2607848/4241180
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes')

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
