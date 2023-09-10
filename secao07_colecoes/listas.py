
"""
listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e tamb-em de podermos colocar QUALUER tipo de dado.

- DINÂMICO: não possui tamanho fixo;
- Qualquer tipo de dado

As listas em Python são representadas por colchete: []
"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

print(lista4)

#  checar se valor está na lista
num = 8
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o numero {num}')
print('------------------------------------')

letra = 'U'  # python é case sensitive
if letra in lista2:
    print(f'Encontrei a letra {letra}')
else:
    print(f'Não encontrei a letra {letra}')
print('------------------------------------')

letra = 'u'  # python é case sensitive
if letra in lista5:
    print(f'Encontrei a letra {letra}')
else:
    print(f'Não encontrei a letra {letra}')
print('------------------------------------')

#  Ordenar uma lista
lista1.sort()
print(lista1)
print('------------------------------------')
lista5.sort()
print(lista5)
print('------------------------------------')

# Contar o número de ocorr~encias em uma lista
print(lista1.count(1))
print(lista5.count('e'))
print('------------------------------------')

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
print('------------------------------------')

"""
- função extend
    só adiciona vários elemento de uma vez
"""
lista1.extend([123, 44, 67])  # coloca elemento na lista como valor adicional.
print(lista1)

# inserir elemento na lista informando a posição (não substitui o valor original), ele é deslocado para direita.
lista1.insert(2, 'Novo valor')
print(lista1)

# juntar listas
"""
lista4.extend(lista5)  # na mesma variável usando extend
print(lista4)

lista4 = lista4 + lista5  # na mesma variável
print(lista4)
"""

lista6 = lista4 + lista5  # em uma nova variável
print(lista6)
