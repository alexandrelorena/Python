"""
Funções com parâmetro

- Pequenas partes de código que realizam tarefas específicas.
- Pode ou não receber entradas de dados e retornar uma saída de dados.
- Muito úteis para executar procedimentos similares repetidas vezes.

Funções com parâmetro >> recebem dados para serem processados dentro das mesmas.

entrada -> processamento -> saída

diferentes tipos e função:

- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

"""

#  Refatorando uma função

print('\n------------Número ao quadrado-----------\n')


def quadrado_de_7():
    return 7 * 7


"""print(quadrado_de_7())
print(quadrado_de_7())
print(quadrado_de_7())
print(quadrado_de_7())"""


def quadrado(numero):
    # return numero * numero
    return numero ** 2


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))
print(quadrado(3))

print('\n------------Número ao cubo-----------\n')


def cubo(numero):
    # return numero * numero * numero
    return numero ** 3


print(cubo(7))
print(cubo(2))
print(cubo(5))
print(cubo(3))


print('\n------------Cantar parabéns-----------\n')

#  refatorando a função


def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o/a {aniversariante}!')


cantar_parabens('Alexandre')

print('\n------------Função com mais de 1 parâmetro-----------\n')


def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(soma(10, 20))
print('\n-----------------------\n')
print(multiplica(4, 5))
print(multiplica(2, 8))
print('\n-----------------------\n')
print(outra(3, 2, 'Geek '))  # multiplicando o resultado da soma pela mensagem
print('\n-----------------------\n')
print(outra(4, 5, 'Python '))  # multiplicando o resultado da soma pela mensagem

print('\n------------Nomeando parâmetros-----------\n')


def nome_completo(string1, string2):
    return f'Seu nome completo é {string1} {string2}'


print(nome_completo('Angelina', 'Jolie'))

print('\n----------------------------------------------\n')


def nome_completo(nome1, sobrenome1):
    return f'Seu nome completo é {nome1} {sobrenome1}'


print(nome_completo('Angelina', 'Jolie'))


print('\n------------Diferença entre parâmetros e argumentos-----------\n')

print('Parâmetros: variáveis declaradas na definição da função;\n')

print('Argumentos: dados passados durante a execução de uma função;\n')

print('\n------------A ordem dos parâmetros importa-----------\n')

nome = 'Felicity'
sobrenome = 'Jones'
print(f'Nome: {nome}')
print('\n----------------------------------------------\n')
print(f'Sobrenome: {sobrenome}')
print('\n----------------------------------------------\n')
print(nome_completo(sobrenome, nome))

print('\n--------------Keyword Arguments------------------\n')

print(nome_completo(nome1='Angelina', sobrenome1='Jolie'))

print(nome_completo(nome1=nome, sobrenome1=sobrenome))

print(nome_completo(sobrenome1='Marques', nome1='Marcia'))

print('\n--------------Erro comum no uso do return------------------\n')

print('\n---------------- ↓ Errado ↓ ----------------\n')


"""def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
        return total  # o return deve ser  embaixo do for


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))
print(type(lista))

tupla = 1, 2, 3, 4, 5, 6, 7
print(soma_impares(tupla))
print(type(tupla))"""

print('\n---------------- ↓ Certo ↓ ----------------\n')


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))
print(type(lista))

tupla = 1, 2, 3, 4, 5, 6, 7
print(soma_impares(tupla))
print(type(tupla))
