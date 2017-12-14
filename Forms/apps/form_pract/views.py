from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'form_pract/index.html')

def new(request):
    if request.method == "POST":
        request.session['name'] = request.POST['first_name']
        request.session['alias'] = request.POST['alias']
    return render(request, 'form_pract/result.html')
