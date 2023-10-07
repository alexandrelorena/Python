"""
Dictionary Comprehension

lista = [1, 2, 3, 4]

tupla = (1, 2, 3, 4)  #1, 2, 3, 4

conjunto/set = {1, 2, 3, 4}

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Síntaxe

{chave:valor for valor in iteravel}

"""
print('\n------------- ↓ Exemplo 1 ↓ -------------\n')

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(numeros)
print(type(numeros))

print('\n------------- ↓ Exemplo 2 - quadrado ↓ -------------\n')

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)
print(type(quadrado))

print('\n------------- ↓ Exemplo 3 - quadrado > chave:valor ↓ -------------\n')

numeros = [1, 2, 3, 4, 5]

quadrados = {valor: valor ** 2 for valor in numeros}

print(quadrados)

print('\n------------- ↓ Exemplo 4 - string e lista ↓ -------------\n')

chaves = 'abcde'

valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}

print(mistura)

print('\n------------- ↓ Exemplo 5 - lógica condicional ↓ -------------\n')

numeros = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}

print(res)
