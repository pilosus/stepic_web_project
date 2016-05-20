# -*- encoding: utf-8; -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=False)
    rating = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # http://stackoverflow.com/a/2607848/4241180
    #author = models.OneToOneField(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes')

    def __unicode__(self):
        """Representation of the instance in admin panel and shell"""
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=False)
    #question = models.OneToOneField(Question, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return "Answer by {0} to question {1}: {2}...".\
            format(self.author.username, self.question.id, self.text[:50])
    
