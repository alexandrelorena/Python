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

print(f'Ordenando com sorted, por valor: {dicionario_ordenado}')

# ------------------------------ ↓  ↓ -------------------------------------

