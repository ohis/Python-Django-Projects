from __future__ import unicode_literals

from django.db import models
import bcrypt

# Create your models here.
class WishManager(models.Manager):
    def create_item(self,new_item,user):
        if len(new_item) == 0:
            return(False)
        if len(new_item) < 3:
            return (False)
        else:
            items = Wish.objects.create(item_name=new_item,creator=User.objects.get(id=user))
            items.save()
        return (True,items)

class UserManager(models.Manager):
    def login(self,usern,password):
        passwd = password.encode()
        hashed = bcrypt.hashpw(passwd,bcrypt.gensalt())
        if User.objects.filter(password=hashed) == None:
            return(False)
        if len(usern) < 3:
            return(False)
        else:
            user = User.objects.filter(password=hashed)
            return(True,user)


    def register(self,name,username,pwd,cw):
        passwd = pwd.encode()
        hashed = bcrypt.hashpw(passwd,bcrypt.gensalt())
        if bcrypt.hashpw(passwd, hashed) == hashed:
            print('it matches')
        if len(name) < 3:
            return (False)
        elif len(username) < 3:
            return(False)
        elif len(pwd) < 8:
            return (False)
        elif not len(cw) == len(pwd):
            return(False)
        else :
            user = User.objects.create(name=name,username=username,password=hashed)
            user.save()
            return (True,user)
class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
class Wish(models.Model):
    item_name = models.CharField(max_length=100)
    wish_item = models.ManyToManyField(User,related_name= 'wishes')
    creator = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WishManager()
    def __str__(self):
        return self.item_name
