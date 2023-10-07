
"""
**kwargs

Exige parâmetros nomeados e os transformam em um dicionário.

Este parâmetro não tem valores obrigatórios (pode ser declarado vazio).

Funções podem ter (NESTA ORDEM!!!):

- Parâmetros obrigatórios;
- *args;
- Parâmetros default (não obrigatórios);
- **kwargs

"""

print('\n---------------- ↓ **kwargs ↓ ----------------\n')

#  exemplo


def cores_favoritas(**kwargs):
    print(kwargs)


cores_favoritas(marcos='verde', julia='anarelo', fernanda='azul', vanessa='branco')

# {'marcos': 'verde', 'julia': 'anarelo', 'fernanda': 'azul', 'vanessa': 'branco'} >> dicionário


print('\n---------------- ↓ **kwargs - iterando no dicionário ↓ ----------------\n')


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')


print('\n---------------- ↓ **kwargs - ex mais complexo ↓ ----------------\n')


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem você é...'


print(cumprimento_especial())

print(cumprimento_especial(geek='Python'))

print(cumprimento_especial(geek='Oi'))

print(cumprimento_especial(geek='especial'))

print('\n---------------- ↓ Funções podem ter (NESTA ORDEM!!!): ↓ ----------------\n')

"""
- Parâmetros obrigatórios;
- *args;
- Parâmetros default (não obrigatórios);
- **kwargs

"""


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, '  Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

print('\n---------------- ↓ kwargs - Desempacotamento ↓ ----------------\n')


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))


print('\n---------------- ↓ kwargs - outro exemplo ↓ ----------------\n')


def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


soma_multiplos_numeros(2, 4, 6)


lista = [1, 2, 3]
print(type(lista))
soma_multiplos_numeros(*lista)

tupla = (2, 3, 4)
print(type(tupla))
soma_multiplos_numeros(*tupla)

conjunto = {3, 4, 5}
print(type(conjunto))
soma_multiplos_numeros(*conjunto)


dicionario = dict(a=4, b=5, c=6)  # No dicionário, os nomes das chaves tem que ser o mesmo os parâmetros da função
print(type(dicionario))
soma_multiplos_numeros(**dicionario)
