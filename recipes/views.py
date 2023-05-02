from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Lucas 1')

def contato(request):
    return render(request, 'Lucas 2')