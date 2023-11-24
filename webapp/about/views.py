from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'name': 'erga',
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'name': 'erga',
    }
    return render(request, 'about.html', context)