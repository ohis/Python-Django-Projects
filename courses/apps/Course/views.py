from django.shortcuts import render,redirect
from .models import*

# Create your views here.
def index(request):
    course = Course.objects.all()
    context = {
      'course':course
    }
    return render(request,'Course/index.html',context)

def create(request):
    if request.method == 'POST':
        course = Course.objects.create(name=request.POST['name'], Description=request.POST['description'])
        print "Success"
        return redirect('/')
    else:
        print 'failed'
        return redirect('/')

def remove(request,id):
    remove_course = Course.objects.get(id=id)
    print "About to remove course"
    context = {
      'remove': remove_course
    }
    return render(request,'Course/delete.html',context)

def destroy(request,id):
    print Course.objects.get(id=id)
    delete_course = Course.objects.get(id=id).delete()
    print delete_course
    print "Deleted"
    return redirect('/')
