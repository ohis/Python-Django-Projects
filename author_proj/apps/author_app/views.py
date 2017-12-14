from django.shortcuts import render
from models import Author,Book

# Create your views here.
def index(request):


    Book.objects.book()
    #books = Book.objects.filter(author=this_author)
    #print "THIS BOOKS",books
    #disp = Book.objects.all()
    #print disp
    #context = {"authors": Author.objects.all()}
    return render(request, "index.html")
