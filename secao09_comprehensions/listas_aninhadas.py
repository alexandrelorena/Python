"""
listas Aninhadas

Em outras linguagens:
- unidimensionais >> Arrays/Vetores
- multidimensionais >> Matrizes

Em Python temos as Listas aninhadas:

numeros = [1, 'b', 3.234, True, 5]

"""
print('\n------------- ↓ Exemplo 1 - Matriz 3 x 3 ↓ -------------\n')

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3

print(listas)
print(type(listas))

print('\n------------- ↓ Exemplo 2 - acessando os dados ↓ -------------\n')

print(listas[2][2])  # 9 >> lista 2 (0, 1, 2) ,índice 2 (0, 1, 2)
print(listas[2][-1])

print('\n------------- ↓ Iterando com loops ↓ -------------\n')

for lista in listas:
    for num in lista:
        print(num)

print('\n------------- ↓ Iterando com List Comprehension ↓ -------------\n')

[[print(valor) for valor in lista] for lista in listas]

print('\n------------- ↓ Gerando um tabuleiro/matriz 3x3 ↓ -------------\n')

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]

print(tabuleiro)

print('\n------------- ↓ Gerando jogo da velha ↓ -------------\n')

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]

print(velha)

print('\n------------- ↓ Gerando valores iniciais no jogo da velha ↓ -------------\n')

print([['*' for i in range(1, 4)] for j in range(1, 4)])
