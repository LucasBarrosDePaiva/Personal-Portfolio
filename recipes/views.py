from django.shortcuts import HttpResponse, render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html')


def contato(request):
    return HttpResponse('contato')
