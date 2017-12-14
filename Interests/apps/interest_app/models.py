from __future__ import unicode_literals

from django.db import models

# Create your models here.
class InterestManager(models.Model):
    def index():
        return True
class UserManager(models.Manager):
    def index():
        return True

class Interest(models.Model):
    interest = models.TextField(max_length=1000)
    #user = models.ManyToManyField(User, related_name='interests')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = InterestManager()
class User(models.Model):
    name = models.CharField(max_length=100)
    user_interest = models.ManyToManyField(Interest, related_name='interests')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
