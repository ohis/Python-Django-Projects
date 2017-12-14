from __future__ import unicode_literals
import bcrypt
from django.db import models
from django.contrib import messages

# Create your models here.
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')


# Create your models here.
class QuoteManager(models.Manager):
    def remove(self,request,id):
        user = User.objects.get(id=request.session['user_id'])
        quote = Quote.objects.get(id=id)
        quote.favorite.remove(user)

        return True

    def add(self,request,id):
        user = User.objects.get(id=request.session['user_id'])
        quote = Quote.objects.get(id=id)
        quote.favorite.add(user)

        return True

    def quote(self, request):
        print request.POST
        errors = []
        if len(request.POST['author']) < 4:
            errors.append('Author name must be more than 3 characters.')
        if len(request.POST['message']) < 10:
            errors.append('Quote must be more than 10 characters.')

        if len(errors) > 0:
            return (False,errors)
        else:
            new_quote = {
                'author': request.POST['author'],
                'message': request.POST['message'],
                'user_submit': User.objects.get(id=request.session['user_id'])
            }
            print new_quote
            quote = Quote.objects.create(**new_quote)
            quote.save()

            return (True,quote)


class UserManager(models.Manager):
    def login(self,email,passwd):
        old_user = self.filter(email=email).first()
        if len(email) < 2 :
            print "ERROR"
            return False
        if not self.filter(password=passwd) == old_user.password:
            return (False)
        elif self.filter(email=email).first() == None :
            return(False)
        else:
          #old_user = self.filter(email=email).first()
          if not old_user == None:
              #odd = old_user.first_name
              return (True,old_user)



    def register(self,first_name,last_name,email,pwd):
            error = []
            if len(first_name) < 2 or not NAME_REGEX.match(first_name):
                error.append("Invalid First Name")
                print "Failed"

            if len(last_name ) < 2 or not NAME_REGEX.match(last_name):
                error.append("Invalid Last Name")
                print "fail"

            if not EMAIL_REGEX.match(email):
                error.append("Invalid Email")
                print "NO EMAIL"

            if len(error) > 0:
                 return(False,error)
            else:
                user = User.objects.create(first_name=first_name,last_name=last_name,email=email,password=pwd)
                user.save()
                #new = user.first_name
                return(True,user)



class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    password = models.CharField(max_length=255)
    objects = UserManager()

    def __str__(self):
        return self.first_name+" "+self.last_name+" "+self.email
class Quote(models.Model):
    author = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    favorite = models.ManyToManyField(User,related_name='favorite')
    user_submit = models.ForeignKey(User,related_name='quote')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = QuoteManager()
    def __str__(self):
        return self.author+" "+self.message
