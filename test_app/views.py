from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        'context_var': 'I am from home view of Django Application'
        }
    return render(request, 'home.html', context)