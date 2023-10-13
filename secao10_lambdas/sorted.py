"""
Sorted

- Não confundir com a função sort();
- Pode ser usado com qualquer iterável;
- Serve para ordenar;
- gera sempre uma lista,

"""
# ------------------------------ ↓ Sorted com lista ↓ -------------------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ Sorted com lista ↓'.center(70)}\033[33m\n{'-' * 70}\033[0m")

numeros = [6, 1, 8, 2]  # o sorted() gera sempre uma lista, indepente se a entrada for lista, tupla, etc

print(numeros)
print(type(numeros))

print(f'Ordenando com sorted(): {sorted(numeros)}')

print(numeros)
print(type(numeros))

# ------------------------------ ↓ Sorted ↓ -------------------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ Sorted com tupla ↓'.center(70)}\033[33m\n{'-' * 70}\033[0m")

numeros = (6, 1, 8, 2)  # o sorted() gera sempre uma lista, indepente se a entrada for lista, tupla, etc
print(numeros)
print(type(numeros))

print(f'Ordenando com sorted(): {sorted(numeros)}')  # Ordenar do menor para o maior
# gera uma nova lista ordena. A lista original permanece intacta.
print(numeros)
print(type(numeros))

# ------------------------------ ↓ Sorted com tupla ↓ -------------------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ Sorted com set ↓'.center(70)}\033[33m\n{'-' * 70}\033[0m")

numeros = {6, 1, 8, 2}  # o sorted() gera sempre uma lista, indepente se a entrada for lista, tupla, etc

print(numeros)
print(type(numeros))

print(f'Ordenando com sorted(): {sorted(numeros)}')

print(numeros)
print(type(numeros))

# ------------------------------ ↓ Sorted com dicionário ↓ -------------------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ Sorted com dicionário ↓'.center(70)}\033[33m\n{'-' * 70}\033[0m")

numeros = [6, 1, 8, 2]  # o sorted() gera sempre uma lista, indepente se a entrada for lista, tupla, etc

print(numeros)
print(type(numeros))

dicionario = {indice: valor for indice, valor in enumerate(numeros)}
print(dicionario)
print(type(dicionario))

# ------------------------------ ↓ por chave ↓ -------------------------------------

print(f"{'↓ por chave ↓'.center(70)}\n")
print("print(f'Ordenando com sorted, por chave: {sorted(dicionario)}')\n")
print(f'Ordenando com sorted, por chave: {sorted(dicionario)}\n')

print(numeros)
print(type(numeros))

# ------------------------------ ↓ por valor ↓ -------------------------------------

print(f"{'↓ por valor ↓'.center(70)}\n")
print("dicionario_ordenado = dict(sorted(dicionario.items(), key=lambda item: item[1]))\n")
dicionario_ordenado = dict(sorted(dicionario.items(), key=lambda item: item[1]))

print(f'Ordenando com sorted, por valor: {dicionario_ordenado}\n')

# ------------------------------ ↓ Ordenar do menor para o maior ↓ -------------------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ Ordenar do menor para o maior ↓'.center(70)}\033[33m\n{'-' * 70}\033[0m")

numeros = [6, 1, 8, 2]  # o sorted() gera sempre uma lista, indepente se a entrada for lista, tupla, etc

print(sorted(numeros))

# ------------------------------ ↓ Ordenar do maior para o menor ↓ -------------------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ Ordenar do maior para o menor ↓'.center(70)}\033[33m\n{'-' * 70}\033[0m")

numeros = [6, 1, 8, 2]  # o sorted() gera sempre uma lista, indepente se a entrada for lista, tupla, etc

print(sorted(numeros, reverse=True))

# ------------------------------ ↓ Ordenar pelo username - ordem alfabética ↓ -------------------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ Ordenar pelo username - ordem alfabética ↓'.center(70)}\033[33m\n{'-' * 70}\033[0m")

usuarios = [  # cada elemento nessa lista é um dicionário
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gost de cachorros", "Eu vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
]

print(usuarios)

print(sorted(usuarios, key=lambda usuario: usuario["username"]))
#  print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=False))

# ------------------------------ ↓ Ordenar pelo número de tweets ↓ -------------------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ Ordenar pelo número de tweets ↓'.center(70)}\033[33m\n{'-' * 70}\033[0m")

usuarios = [  # cada elemento nessa lista é um dicionário
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gost de cachorros", "Eu vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
]

print(usuarios)

print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"]), reverse=True))

# ------------------------------ ↓ Ordenar músicas ↓ -------------------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ Ordenar músicas ↓'.center(70)}\033[33m\n{'-' * 70}\033[0m")

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'n roll, too yung to die", "tocou": 32},
]

print(f"{'↓ Menos tocada para mais tocada ↓'.center(70)}\n")

print(sorted(musicas, key=lambda musica: musica['tocou']))

print(f"\n{'↓ Mais tocada para menos tocada ↓'.center(70)}\n")

print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
