from __future__ import unicode_literals
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
import bcrypt
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class ClientManager(models.Manager):
    def index():
        return True
class ProjectManager(models.Manager):
    def index():
        return True
class Client(models.Model):
    business_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    # message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    #phone_number = models.CharField(validators=[phone_regex],max_length=15, blank=True) # validators should be a list
    phone_number = PhoneNumberField()
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ClientManager()


class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client,related_name="projects")
    project_notes = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProjectManager()
