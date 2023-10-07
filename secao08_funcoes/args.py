
"""
Entendendo o *args

O *args é um parâmetro como qualquer outro.
Podemos chamar qualquer coisa desde que comece com *.

Esse parâmetro utilizado em uma função, coloca os vaores extras informados em uma tupla.

Este parâmetro não tem valores obrigatórios (pode ser declarado vazio).

ex: def soma_todos_numeros(*args):
    print(args)  # printando os argumentos

    soma_todos_numeros()

"""
#  Exemplos


def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(2, 1, 8))

# print(soma_todos_numeros(3, 2, 1, 8))  # TypeError


print('\n---------------- ↓ Com valor padrão ↓ ----------------\n')


def soma_todos_numeros(num1=1, num2=2, num3=3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))

print(soma_todos_numeros(4, 6))


# print(soma_todos_numeros(3, 2, 1, 8))  # TypeError


print('\n---------------- ↓ Entendendo o args ↓ ----------------\n')


def soma_todos_numeros(*args):
    print(args)  # printando os argumentos


soma_todos_numeros()
soma_todos_numeros(1)
soma_todos_numeros(2, 3)
soma_todos_numeros(2, 3, 4)
soma_todos_numeros(3, 4, 5, 6)


def soma_todos_numeros(*args):
    return sum(args)  # usando função sum com tupla


"""    total = 0
    for numero in args:
        total = total + numero
    return total"""

# somente números inteiros ou reais:
print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(3, 4, 5, 6))
print(soma_todos_numeros(23.4, 12.5))

print('\n---------------- ↓ Args com valores obrigatórios ↓ ----------------\n')


def soma_todos_numeros(nome, email, *args):
    return sum(args)  # usando função sum com tupla


# somente números inteiros ou reais:
print(soma_todos_numeros('Angelina', 'Jolie'))
print(soma_todos_numeros('Angelina', 'Jolie', 1))
print(soma_todos_numeros('Angelina', 'Jolie', 2, 3))
print(soma_todos_numeros('Angelina', 'Jolie', 2, 3, 4))
print(soma_todos_numeros('Angelina', 'Jolie', 3, 4, 5, 6))
print(soma_todos_numeros('Angelina', 'Jolie', 23.4, 12.5))

print('\n---------------- ↓ Args - outro exemplo ↓ ----------------\n')


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não tenho certeza quem você é...'


print(verifica_info())

print(verifica_info(1, True, 'Geek', 'University'))

print(verifica_info('Geek'))

print(verifica_info('University'))

print(verifica_info('Geek University'))

print(verifica_info('Geek', 'University'))


print('\n---------------- ↓ Args - Desempacotamento ↓ ----------------\n')


def soma_todos_numeros(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6, 7]  # lista
print(type(numeros))

numeros2 = {1, 3, 4, 6, 7}  # conjunto
print(type(numeros2))

numeros3 = (1, 3, 6, )  # tupla
print(type(numeros3))

print(soma_todos_numeros(*numeros))  # o * mostra ao python que o argumento é uma coleção de dados.

print(soma_todos_numeros(*numeros2))

print(soma_todos_numeros(*numeros3))
