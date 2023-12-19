from django.shortcuts import render


def index(request):
    print(dir(request.user))
    print(f"User: {request.user}")

    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não está logado'
    else:
        teste = 'Usuário logado!'
    context = {
        'curso': 'Programação Web com Django FrameWork',
        'outro': 'Django é massa!',
        'logado': teste
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
