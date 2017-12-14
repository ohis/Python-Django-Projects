from __future__ import unicode_literals

from django.db import models
#one tomany relationship
# Create your models here.
class AuthorManager(models.Manager):
    def index():
        return True
class BookManager(models.Manager):
    def book(self):
        autor1 = Author.objects.create(name='Jane Austen')
        autor2 = Author.objects.create(name='Douglas Adams')
        print autor2
        autor3 = Author.objects.create(name='Philip Roth')
        autor4 = Author.objects.create(name='Stephen Hawking')
        autor5 = Author.objects.create(name='Louisa My Alcott')

        this_author = Author.objects.filter(id=2)
        my_book = Book.objects.create(title="Little Women", author=this_author)
        print this_author
        #this_author2 = Author.objects.get(id=3)
        #this_author3 = Author.objects.get(id=4)
        #this_author4 = Author.objects.get(id=5)



        return Author.objects.all()
class Author(models.Model):
    name = models.CharField(max_length =255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()

    #def __str__(self):
    #    return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author,related_name="books")
    books = models.ManyToManyField(Author,related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BookManager()

    #def __str__(self):
    #    return self.title

class Publisher(models.Model):
	name = models.CharField(max_length=255)
	books = models.ManyToManyField(Book, related_name="publishers")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
