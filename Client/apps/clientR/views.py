from django.shortcuts import render,redirect

  # Inside your app's views.py file
from django.core.urlresolvers import reverse

from .models import*
# Create your views here.
def index(request):
    context ={
       'clients': Client.objects.all()
    }
    return render(request, 'clientR/index.html',context)
def new(request):
    return render(request,'clientR/new.html')
def create(request):
    if request.method == 'POST':

        new_client = Client.objects.create(business_name=request.POST['biz_name'],
         email=request.POST['email'],phone_number=request.POST['phone'],notes=request.POST['notes'])
        return redirect(reverse('my_index'))
    else:
        print "Error"
        return redirect(reverse('new_client'))

def show(request,id):
    biz = Client.objects.get(id=id)
    print biz.email
    context = {
    'biz':biz
    }

    return render(request, 'clientR/show.html',context)

def addProject(request,id):
    if request.method == 'POST':
        new_project = Project.objects.create(project_name=reques.POST['proj_name'],
        notes=request.POST['notes'],client=Client.objects.get(id=id))
        context ={
         'proj': Project.objects.get(id)
        }

    else:
        print "Failed to add project"
        return redirect(reverse('new_project'))
