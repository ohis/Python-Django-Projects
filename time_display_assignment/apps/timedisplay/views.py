from django.shortcuts import render,HttpResponse
import datetime
#contoller
# Create your views here.
def index(request):
    context ={
    'date':datetime.datetime.now()

    }
    return render(request,'timedisplay/index.html',context)
