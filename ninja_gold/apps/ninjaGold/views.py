from django.shortcuts import render,redirect,HttpResponse
from random import randint
import datetime

# Create your views here.

def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
        print "yay"
    if not 'events' in request.session:
        request.session['events'] = []
    return render(request,'ninjaGold\index.html')

def process(request):
    print "got here"
    if request.method == 'POST':
            print "ok good moveon"
    building = request.POST['building']
    if building == 'farm' :
         result = randint(15,20)
         request.session['gold'] = result
    elif building == 'cave':
           result = randint(5,10)
           request.session['gold']  = result
    elif building == 'house' :
           result = randint(2,5)
           request.session['gold']  = result
    elif building == 'casino' :
           result = randint(-50,50)
           print result
           if result < 0 :
               res = abs(result)
               request.session['gold']  = res
               print "A negative number :",res
           else:
              request.session['gold']  = result
    print request.session['events']

    if result > 0 :
        request.session['events'].append("Earned {} gold from the {} at {}".format(result,building,datetime.datetime.now()))
    else:
        request.session['events'].append("Entered a casino and lost {} gold...Ouch..".format(res,building,datetime.datetime.now()))

    return redirect('/')

"""def  cave(request):
    print "got here"
    if request.method == 'POST':
        print "ok good moveon"
        randNum = randint(5,10)
        request.session['val_cave'] = randNum
        print request.session['val_cave']
    return redirect('/')

def  house(request):
    print "got here"
    if request.method == 'POST':
        print "ok good moveon"
        randNum = randint(2,5)
        request.session['val_house'] = randNum
        print request.session['val_house']
        print request.form['building']
    return redirect('/')

def  casino(request):
    print "got here"
    if request.method == 'POST':
        print "ok good moveon"
        randNum = randint(-50,50)
        request.session['val_casino'] = randNum
        print request.session['val_casino']
    return redirect('/')
"""
