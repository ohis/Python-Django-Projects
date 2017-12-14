from django.shortcuts import render,redirect
from .models import*

# Create your views here.
def index(request):
    context = {
        'authors' : Book.objects.all()
    }
    return render(request, 'stackbook/index.html', context)

def create(request):
    if request.method == 'POST' :
        print 'got here'
        book = Book.objects.create(title=request.POST['title'],
        author=request.POST['author'],category=request.POST['category'])
        return redirect('/')
    else:
        print "Error"
        return redirect('/')
