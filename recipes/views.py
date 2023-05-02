from django.shortcuts import HttpResponse, render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html')


def contato(request):
    return render(request, 'recipes/contato.html')
    # return render(request, 'recipes/contato.html') -> Retorna o que está no arquivo
    # return HttpResponse('Retorna o que está escrito aqui dentro')
