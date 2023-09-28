
"""
listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e tamb-em de podermos colocar QUALUER tipo de dado.

- DINÂMICO: não possui tamanho fixo;
- Qualquer tipo de dado
- Litas são mutáveis
As listas em Python são representadas por colchete: []
"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

print(lista4)

print('\n----------------------------- Checar valor em uma lista ------------------------------\n')

#  checar se valor está na lista
num = 8
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o numero {num}')

print('\n------------------------------------\n')

letra = 'U'  # python é case sensitive
if letra in lista2:
    print(f'Encontrei a letra {letra}')
else:
    print(f'Não encontrei a letra {letra}')

print('\n------------------------------------\n')

letra = 'u'  # python é case sensitive
if letra in lista5:
    print(f'Encontrei a letra {letra}')
else:
    print(f'Não encontrei a letra {letra}')

print('\n----------------------------- Ordenar uma lista ------------------------------\n')
lista1.sort()
print(lista1)

print('\n------------------------------------\n')
lista5.sort()
print(lista5)

print('\n------------------------------------\n')
# Contar o número de ocorrências em uma lista
print(lista1.count(1))
print(lista5.count('e'))

print('\n----------------------------- Adicionar em uma lista ------------------------------\n')
"""
Adicionar elementos em uma lista 
- função append
    só adiciona 1 elemento por vez
"""
print(lista1)
lista1.append(42)
print(lista1)

# lista dentro de outra lista
lis = [8, 3, 1]
lista1.append([8, 3, 1])  # coloca a lista como elemento único (sublista)
print(lista1)

if lis in lista1:
    print(f'Encontrei a lista {lis}')
else:
    print(f'Não encontrei a lista {lis}')

"""
- função extend
    só adiciona vários elemento de uma vez
"""
lista1.extend([123, 44, 67])  # coloca elemento na lista como valor adicional.
print(lista1)

# inserir elemento na lista informando a posição (não substitui o valor original), ele é deslocado para direita.
lista1.insert(2, 'Novo valor')
print(lista1)

print('\n------------------------------- Juntar listas -------------------------------\n')
"""
lista4.extend(lista5)  # na mesma variável usando extend
print(lista4)

lista4 = lista4 + lista5  # na mesma variável
print(lista4)
"""

lista6 = lista4 + lista5  # em uma nova variável
print(lista6)

print('\n---------------------------- Inverter uma lista -----------------------------\n')
"""  
Inverter listas
    - Forma 1 - reverse
"""
lista1.reverse()
print(lista1)

lista2.reverse()
print(lista2)

"""  
Inverter listas
    - Forma 2 - slice
"""
print(lista1[::-1])

print(lista2[::-1])

print('\n----------------------------- Copiar uma lista ------------------------------\n')
# Copiar uma lista
lista7 = lista2.copy()
print(lista2)
print(lista7)

print('\n----------------------------- Contar elementos da lista ------------------------------\n')
print('lista 1 tem ', len(lista1), 'elementos')
print('lista 2 tem ', len(lista2), 'elementos')
print('lista 3 tem ', len(lista3), 'elementos')
print('lista 4 tem ', len(lista4), 'elementos')
print('lista 5 tem ', len(lista5), 'elementos')
print('lista 6 tem ', len(lista6), 'elementos')
print('lista 7 tem ', len(lista7), 'elementos')

print('\n----------------------------- Remover último elemento da lista ------------------------------\n')
print(lista5)
lista5.pop()  # Além de remover o último elemento, retorna esse elemento
print(lista5)

print('\n----------------------------- Remover índice da lista ------------------------------\n')
print(lista5)
lista5.pop(2)  # Além de remover o último elemento, retorna esse elemento.
# Elementos à direita são deslocaados para a esquerda.
print(lista5)

print('\n----------------------------- Remover lista ------------------------------\n')
print(lista5)
lista5.clear()
print(lista5)

print('\n----------------------------- Repetir elementos na lista ------------------------------\n')
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

print('\n----------------------------- Converter String para lista ------------------------------\n')
#  Exemplo 1
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

#  Exemplo 2
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

print('\n----------------------------- Converter Lista para String ------------------------------\n')
lista8 = ['Programação', 'em', 'Python:', 'Essencial']  # lista
print(lista8)
curso = ' '.join(lista8)  # string
print(curso)

teste = 'Programação em Python: Essencial'

lista_nova = list(teste)   # lista
print(lista_nova)
lista_nova = '|'.join(lista_nova)  # string
print(lista_nova)

print('\n----------------------------- Iterando sobre Listas ------------------------------\n')
# Exemplo 1 - utilizando for
soma = ''
lista2.reverse()
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - utilizando while
carrinho = []
produto = ''

"""while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair:")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
"""
print('\n----------------------------- Valores fixos e variáveis ------------------------------\n')
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros2 = [num1, num2, num3, num4, num5]
print(numeros2)

print('\n----------------------------- acessando elementos de forma inversa ------------------------------\n')
#           0         1        2         3
cores = ['verde', 'amarelo', 'azul', 'branco']
#           -4        -3       -2       -1
print(cores[-1])

print('\n----------------------------- Gerar índice em um for ------------------------------\n')

cores = ['verde', 'amarelo', 'azul', 'branco']
for indice, cor in enumerate(cores):
    print(indice, cor)

print('\n----------------------------- Encontrar um índice de um elemento na lista ------------------------------\n')
numeros = [5, 6, 7, 8, 9, 10, 5, 11]

print('O número 8 está na posição', numeros.index(8))
print('O número 5 está na posição', numeros.index(5))  # retorna o índice do primeiro elemento duplicado encontrado
print('O número 10 está na posição', numeros.index(10))

print('O número 5 está na posição', numeros.index(5, 1))  # retorna o índice do primeiro elemento duplicado encontrado a
# partir do índice indicado

print('O número 5 está na posição', numeros.index(5, 1, 7))  # retorna o índice do primeiro elemento duplicado
# encontrado a

print('\n----------------------------- Slice ------------------------------\n')
lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista[1:])  # parâmetro início
print(lista[-3:])

print(lista[:2])  # parâmetro fim
print(lista[:-4])

print(lista[1::2])  # parâmetro passo - começa em 1 e vai até o final de 2 em 2

print('\n----------------------------- Invertendo valores em uma lista ------------------------------\n')
nomes = ['Geek', 'University']
print(nomes)

nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes.reverse()
print(nomes)

print('\n----------------------------- Soma, valor máximo, valor mínimo, tamanho ------------------------------\n')
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(lista))  # soma - valor inteiro ou flutuante
print(max(lista))  # valor máximo - valor inteiro ou flutuante
print(min(lista))  # valor mínimo - valor inteiro ou flutuante
print(len(lista))  # tamanho da lista - qualquerr tipo de dado

print('\n----------------------------- Transformar lista em tupla ------------------------------\n')
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

print('\n----------------------------- Desempacotamento de listas ------------------------------\n')
lista = [1, 2, 3]
num1, num2, num3 = lista
#  tem que ter o mesmo número de elementos e variáveis
print(num1)
print(num2)
print(num3)

print('\n----------------------------- Copiando uma lista - Deep copy ------------------------------\n')
#  Shallow copy e deep copy

#  Forma 1 - Deep copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy()  # cópia
print(nova)

nova.append(4)
print(lista)
print(nova)
print('\n----------------------------- Copiando uma lista - Shallow copy ------------------------------\n')

#  Forma 2 - Shallow copy
lista = [1, 2, 3]
print(lista)

nova = lista  # cópia

nova.append(4)

print(lista)
print(nova)
#  Esse tipo de cópia altera os elemnentos nas 2 listas
