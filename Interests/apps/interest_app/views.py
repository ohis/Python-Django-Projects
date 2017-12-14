from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from .models import*

# Create your views here.

def index(request):
    return render(request, 'interest_app/index.html')
def show(request):
    return render(request,'interest_app/show.html')

def delete(request,id):
    this_user =  User.objects.get(id=request.session['users_id'])
    this_user.user_interest.get(id=id).delete()
    return redirect(reverse('show_page',kwargs={'id':request.session['users_id']}))



def add(request):
    if request.method == 'POST':
                print 'First Step'
                if not  User.objects.filter(name=request.POST['name']).exists():
                    if request.POST['name'] != '':
                    #if not Interest.objects.filter(interest=request.POST['interest']).exists():
                          user = User.objects.create(name=request.POST['name'])
                          new = User.objects.get(id=user.id)
                          request.session['users_id'] = user.id

                          first_interest = Interest.objects.create(interest= request.POST['interest'])
                          new.user_interest.add(Interest.objects.get(id=first_interest.id))
                          request.session['interest_id'] = first_interest.id
                       #return render(request,'interest_app/next.html')
                else:
                    old_user = User.objects.get(name=request.POST['name'])
                    old = User.objects.get(id=old_user.id)
                    if not old.user_interest.filter(interest=request.POST['interest']).exists():
                     #user = User.objects.create(name=request.POST['name'])
                     #Interest.objects.create(interest= request.POST['interest'])
                             interest = Interest.objects.create(interest= request.POST['interest'])
                             old_user = User.objects.get(name=request.POST['name'])
                             print old_user.id
                             old = User.objects.get(id=old_user.id)
                             old.user_interest.add(Interest.objects.get(id=interest.id))
                    #return render(request,'interest_app/next.html')

    context = {
      'all_users': User.objects.all()
    }

    return render(request,'interest_app/next.html',context)





def back_to_index(request):
    return redirect(reverse('my_index'))

def back_to_next(request):
    return redirect(reverse('users_page'))

def show(request,id):
    personal_interest = User.objects.get(id=id)
    request.session['users_id'] = id
    print id
    print request.session['users_id']
    context = {
     "user":personal_interest,
     "user_interest":personal_interest.user_interest.all()
    }

    return render(request, 'interest_app/show.html',context)
