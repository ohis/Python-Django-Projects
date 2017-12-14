from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    if not 'count' in request.session:
        request.session['count'] = 0
    return render(request, 'forms/index.html')

def result(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST.get("location")
        request.session['language'] = request.POST.get("language")
        request.session['comment'] = request.POST.get("comment")
        request.session['count'] +=1
    return render(request, 'forms/result.html')
