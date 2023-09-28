
"""
entendendo_ranges

Ranges são utiliados para gerar sequências numéricas de maneira especificada, não aleatória.

Formas gerais:

# Forma 1

range(valor_de_parada)

OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

# Forma 2

range(valor_de_inicio. valor_de_parada)

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo de 1 em 1).

# Forma 3

range(valor_de_inicio. valor_de_parada, passo)

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário.).

# Forma 4 (inversa)

range(valor_de_inicio. valor_de_parada, passo)

OBS: valor_de_parada não inclusive (valor_de_inicio especificado pelo usuário, e passo especificado pelo usuário.).


"""

# Forma 1
print('\033[97;40mForma 1: for num in range(11):\033[0m')
for num in range(11):
    print(num)
print('\n------------------------------------\n')

# Forma 2
print('\033[97;40mForma 2: for num in range(1, 11):\033[0m')
for num in range(1, 11):
    print(num)
print('\n------------------------------------\n')

# Forma 3
print('\033[97;40mForma 3: for num in range(1, 10, 2):\033[0m')
for num in range(1, 10, 2):
    print(num)
print('\n------------------------------------\n')

# Forma 4 (contagem regressiva)
print('\033[97;40mForma 4: for num in range(10, -1, -1):\033[0m')
for num in range(10, -1, -1):
    print(num)
print('\n------------------------------------\n')
