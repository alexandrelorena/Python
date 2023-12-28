from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')

def contato(request):
    return render(request, 'core/contato.html')

def produto(request):
    return render(request, 'core/produtos.html')
