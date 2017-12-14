from django.shortcuts import render,redirect
import bcrypt
from .models import*
# Create your views here.

def index(request):
    return render(request,'belt/index.html')

def remove(request,id):
    if request.method == 'POST':
        Quote.objects.remove(request, id)
        messages.success(request, 'You have removed this quote  from favorites.')

    else:
        messages.error(request, 'Please click on the quote you would like to add to favorites.')
    return redirect('/quotes')


def add(request,id):
    if request.method == 'POST':
        Quote.objects.add(request, id)
        messages.success(request, 'You have added this quote  to favorites.')

    else:
        messages.error(request, 'Please click on the quote you would like to add to favorites.')
    return redirect('/quotes')



def show(request):
    print"AM HERE"
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'quotes': Quote.objects.all().exclude(favorite=user).order_by('-created_at'),
        'quote_favorites': user.favorite.all()
    }
    return render(request, 'belt/quotes.html', context)



def submit(request):
    if request.method == 'POST':
        validate = Quote.objects.quote(request)
        print validate
        if validate[0] == True:
            messages.success(request, 'Successfull submission')

        else:
                messages.error(request, "You had one or more errors during submission")

    else:
        messages.error(request, 'Use form to submit')
    return redirect('/quotes')


def  register(request):
    name = request.POST['first_name']
    lname = request.POST['last_name']
    email = request.POST['email']
    pwd = request.POST['password']
    cpwd = request.POST['pw']
    pwds = pwd.encode()
    cpwds = cpwd.encode()
    if not pwd == cpwd or len(pwd) < 8:
        messages.error(request,"passwords do not match or length too short")
        return redirect('/')
    else:
        hashed1 = bcrypt.hashpw(cpwds, bcrypt.gensalt())
        hashed = bcrypt.hashpw(pwds, bcrypt.gensalt())
        if bcrypt.hashpw(pwds, hashed) == hashed:
           print("It Matches!")


    user = User.objects.register(name,lname,email,pwds)
    if user[0] == False:
        #print  user[1][0]
        print "BOOOSSS"
        messages.error(request, 'One or more of your input is invalid')
        return redirect('/')

    print "here"
    print user
    print 'OK'
    users = User.objects.all()
    print "User id ",user[1].id
    request.session['user_id'] = user[1].id
    print users

    context = {
      'user':User.objects.get(id=request.session['user_id']),
      'message':'registered'
    }


    return render(request,'belt/quotes.html',context)


def log(request):
    pwd = request.POST['password1']
    email = request.POST['email1']
    pwds = pwd.encode()
    if  len(pwd)  < 8:
        messages.error(request,"password invalid  or length too short")
        return redirect('/')
    else:
        hashed = bcrypt.hashpw(pwds, bcrypt.gensalt())
        if bcrypt.hashpw(pwds, hashed) == hashed:
           print("It Matches!")
    user = User.objects.login(email,pwd)
    if user == False:
        messages.error(request, 'Unsuccessful login')
        return redirect('/')
    else:

        print "User id ",user[1].id
        request.session['user_id'] = user[1].id
        #User.objects.get(id=request.session['user_id']),

        context = {
          'user':User.objects.get(id=request.session['user_id']),
          'message': 'logged in'
        }
        return render(request,'belt/quotes.html',context)
