
"""
loop_for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas


for item in interavel:
    //execução do loop

Utilizamos loops para iterar sequências ou sobre valores iteráveis.

Exemplos de iteráveis:
- String
    nome = 'GeekeUniversity'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
'numero = range(1, 10)

"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

# Exemplo de for 1

for letra in nome:
    print(letra)
print('\n--------------------------------------------------------\n')

#  Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)
print('\n--------------------------------------------------------\n')

#  Exemplo de for 3 (iterando sobre um range)
"""
range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.
"""
for numero in range(1, 10):
    print(numero)
print('\n--------------------------------------------------------\n')

#  Índice
"""
Enumerate:
((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'))

"""
for indice, letra in enumerate(nome):
    print(nome[indice])
print('\n--------------------------------------------------------\n')

for indice, letra in enumerate(nome):
    print(letra)
print('\n--------------------------------------------------------\n')

for _, letra in enumerate(nome):  # '_,' descarta o índice.
    print(letra)
print('\n--------------------------------------------------------\n')

for valor in enumerate(nome):
    print(valor)
print('\n--------------------------------------------------------\n')

"""qtd = int(input('Quantas vezes esse loop deve rodar? '))

for n in range(1, qtd):
    print(f'Imprimindo {n}')
print('\n--------------------------------------------------------\n')

soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')
print('\n--------------------------------------------------------\n')"""

nome = 'Geek University'
for letra in nome:
    print(letra, end='')  # "end=''" evita pular linha
print('\n--------------------------------------------------------\n')

# Unicode
""" 
Original: U+1F60D  U+1F680
Modificado: U0001F60D  U0001F680
"""

for num in range(1, 11):
    print('\U0001F680' * num, '\U0001F60D' * num)
# print('\n--------------------------------------------------------\n')

for _ in range(3):
    for num in range(10, 0, -1):
        print('\U0001F680' * num, '\U0001F60D' * num)
print('\n--------------------------------------------------------\n')
# print(('\U0001F680' * num)[::-1])
