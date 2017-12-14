from django.shortcuts import render,redirect
from .models import*

# Create your views here.
def index(request):

    return render(request,'blogs/index.html')

def blogs(request):
    print "Am here"
    bb = request.POST['blog']
    print bb
    blog = Blog.objects.create(title=request.POST['title'],blog=request.POST['blog'])
    request.session['blog_id'] = blog.id
    print request.session['blog_id']
    return redirect('/show')

def show(request):
    print "Almost done"
    print request.session['blog_id']
    blog =  Blog.objects.get(id=request.session['blog_id'])
    print blog
    context = {
     "blogs":Blog.objects.all(),
     "comment":blog.comments.all

    }
    print blog.comments.all

    return render(request,'blogs/index.html',context)
def comments(request,id):
    print"Herrerere"
    blog = Blog.objects.get(id=id)
    com = Comment.objects.create(comment=request.POST['comment'],blog=blog)

    comment = Comment.objects.get(id=com.id)
    print "Got here"
    print com.id
    Comment.objects.add_comment(request,com.id)
    print"left"

    return redirect('/show')
