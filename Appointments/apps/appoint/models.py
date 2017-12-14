from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AppointManager(models.Manager):
    def index():
        return True
class Appoint(models.Model):
    time = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = AppointManager()
