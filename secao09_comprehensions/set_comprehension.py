
"""
Set Comprehension

"""
print('\n------------- ↓ Exemplo 1 ↓ -------------\n')

numeros = {num for num in range(1, 7)}
print(numeros)

print('\n------------- ↓ Exemplo 2 ↓ -------------\n')

numeros = {x ** 2 for x in range(10)}

print(numeros)  # Set não garante a ordem

print('\n------------- ↓ Exemplo 3 - dicionário ao invéz de set ↓ -------------\n')

numeros = {x: x ** 2 for x in range(10)}

print(numeros)

print('\n------------- ↓ Exemplo 4 - strings ↓ -------------\n')

letras = {letra for letra in 'Geek University'}

print(letras)
