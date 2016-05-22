# -*- encoding: utf-8; -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import datetime
#from django.utils.timezone import now

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes')

    def get_url(self):
        return reverse('question', kwargs={'question_id': self.pk})
    
    def __unicode__(self):
        """Representation of the instance in admin panel and shell"""
        return self.title

    

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True,  auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('question', kwargs={'question_id': self.question.id})
    
    def __unicode__(self):
        return "Answer by {0} to question {1}: {2}...".\
            format(self.author.username, self.question.id, self.text[:50])
    
