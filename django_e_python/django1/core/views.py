from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from.models import Produto

def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': 'Programação Web com Django FrameWork',
        'outro': 'Django é massa!',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)

def error404(request, exception):
    return render(request, '404.html', status=404)
def error500(request):
    return render(request, '500.html', status=500)



