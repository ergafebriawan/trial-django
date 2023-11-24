from django.shortcuts import render

# Create your views here.

def blog(request):
    context = {
        'name': 'erga'
    }

    return render(request, 'blog/blog.html', context)
