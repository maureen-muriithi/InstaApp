from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'Welcome to Instagram'
    return render(request, 'instagram/index.html', {"title": title})
