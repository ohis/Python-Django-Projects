from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CommentManager(models.Manager):
    def add_comment(self,request,id):
        blogs = Blog.objects.get(id=request.session['blog_id'])
        print "Closeeee"
        com = Comment.objects.get(id=id)
        print"Outttttttt"
        com.user_comment.add(blogs)
        return True

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Blog(models.Model):
    title = models.CharField(max_length=255)
    blog = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    user_comment = models.ManyToManyField(Blog,related_name='comments')
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CommentManager()

    def __str__(self):
        return self.blog+" "+self.comment+" "+self.user_comment
