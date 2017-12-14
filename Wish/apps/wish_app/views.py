from django.shortcuts import render,redirect
from .models import*
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request,'wish_app/index.html')
def delete_item(request,id):
    item = Wish.objects.filter(id=request.session['item_id'])
    print 'nEDD ITEM ID'
    print item
    item.delete()
    return render(request,'wish_app/wish.html')


def create_item(request):
    if request.method == 'POST':
        new_item = request.POST['item']
        user = request.session['user_id']
        print user
        print"Here"
        item = Wish.objects.create_item(new_item,user)
        if new_item[0] == False:
            messages.error(request,'Unsuccessfull add')
            return render(request,'wish_app/create.html')
        else:
            messages.success(request,'Successfully added')
            request.session['item_id'] = item[1].id
            print item[1].id
            return redirect('/show')
    else:
        messages.error(request,'Some error occured')
        return render(request,'wish_app/create.html')



def add_new(request):
    return render(request,'wish_app/create.html')
def show(request):
    user = User.objects.get(id=request.session['user_id'])
    wish_item = Wish.objects.filter(creator=user)
    other_wishlist = Wish.objects.all().exclude(wish_item=user).exclude(creator=user)
    print user

    context = {
      'user': user,
      'wish_item':wish_item,
      'other_wishlist':other_wishlist
    }

    return render(request,'wish_app/wish.html',context)


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        print name
        username = request.POST['username']
        print username
        pwd = request.POST['password']
        cwd = request.POST['cw']
        user = User.objects.register(name,username,pwd,cwd)
        if user[0] == False:
            messages.error(request,"Try again invalid input")
            return redirect('/')
        else:
            request.session['user_id'] = user[1].id
            messages.success(request,'Successful')
            return redirect('/show')
    else:
        messages.error(request,"some error occured")
        return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['usern']
        password = request.POST['pwd']
        user = User.objects.login(username,password)
        if user[0] == False :
            messages.error(request,"Invalid login")
            return redirect('/')
        else:
            request.session['user_id'] = user[1].id
            messages.success(request,'Successful')
            return redirect('/show')
    else:
        messages.error(request,"some error occured")
        return redirect('/')
