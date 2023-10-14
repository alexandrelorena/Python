"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.

"""
# ------------------------------ ↓ Min e Max ↓ -------------------------------------

print(f"\033[33m{'-' * 90}\n\033[94m{' Min e Max '.center(90)}\033[0m")

# ------------------------- ↓ lista ↓ ----------------------------

print(f"\033[33m{'-' * 90}\n\033[94m{'↓ lista ↓'.center(90)}\033[33m\n{'-' * 90}\033[0m")

lista = [1, 8, 4, 99, 34, 129]

# ------------------------- ↓ max ↓ ----------------------------

print((f"\033[31mlista = {lista} | " + f"\033[36mTipo: {type(lista)}\n\033[0m"))

print(f"\033[31mmax() >> \033[36m{max(lista)} \n\033[0m")

# ------------------------- ↓ min ↓ ----------------------------

print(f"\033[31mmin() >> \033[36m{min(lista)} \033[0m")

# ------------------------- ↓ tupla ↓ ----------------------------

print(f"\033[33m{'-' * 90}\n\033[94m{'↓ tupla ↓'.center(90)}\033[33m\n{'-' * 90}\033[0m")

tupla = (1, 8, 4, 99, 34, 129)

# ------------------------- ↓ max ↓ ----------------------------

print((f"\033[31mtupla = {tupla} | " + f"\033[36mTipo: {type(tupla)}\n\033[0m"))

print(f"\033[31mmax() >> \033[36m{max(tupla)} \n\033[0m")

# ------------------------- ↓ min ↓ ----------------------------

print(f"\033[31mmin() >> \033[36m{min(tupla)} \033[0m")

# ------------------------- ↓ conjunto ↓ ----------------------------

print(f"\033[33m{'-' * 90}\n\033[94m{'↓ conjunto ↓'.center(90)}\033[33m\n{'-' * 90}\033[0m")

conjunto = {1, 8, 4, 99, 34, 129}

# ------------------------- ↓ max ↓ ----------------------------

print((f"\033[31mconjunto = {conjunto} | " + f"\033[36mTipo: {type(conjunto)}\n\033[0m"))

print(f"\033[31mmax() >> \033[36m{max(conjunto)} \n\033[0m")

# ------------------------- ↓ min ↓ ----------------------------

print(f"\033[31mmin() >> \033[36m{min(conjunto)} \033[0m")

# ------------------------- ↓ dicionário ↓ ----------------------------

print(f"\033[33m{'-' * 90}\n\033[94m{'↓ dicionario ↓'.center(90)}\033[33m\n{'-' * 90}\033[0m")

dicionario = {'a': 200, 'b': 8, 'c':  4, 'd': 99, 'e': 34, 'f': 129}

# ------------------------- ↓ max ↓ ----------------------------

print((f"\033[31mdicionario = {dicionario} | " + f"\033[36mTipo: {type(dicionario)}\n\033[0m"))

# ordenado por valor
print(f"\033[31mmax() >> \033[36m{max(dicionario.values())}\033[33m | " f'ordenado por valor' + f" \n\033[0m")

# ordenado por chave
print(f"\033[31mmin() >> \033[36m{min(dicionario)}\033[33m | " f'ordenado por chave' + f" \n\033[0m")

# ------------------------- ↓ recebe 2 valores e mostra o maior ↓ ----------------------------

print(f"\033[33m{'-' * 90}\n\033[94m{'↓ recebe 2 valores e mostra o maior ↓'.center(90)}\033[33m\n{'-' * 90}\033[0m")

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

if val1 == val2:
    print(f'\n\033[37mOs valores \033[31m{val1} \033[37me \033[31m{val2} \033[37msão iguais!\n')
else:
    print((f"\n\033[37mO maior valor é:\033[31m {max(val1, val2)} \033[90m| " + f"\033[37mO menor valor é:\033[31m "
                                                                                f"{min(val1, val2)}\n"))

soma = (max(val1, val2) + min(val1, val2))
subt = (max(val1, val2) - min(val1, val2))
mult = (max(val1, val2) * min(val1, val2))
div = (max(val1, val2) / min(val1, val2))

print(f'\033[37mA soma entre\033[36m {max(val1, val2)} \033[37me\033[36m {min(val1, val2)} \033[37mé:\033[33m {soma}\n')

print(f'\033[37mA subtração entre\033[36m {max(val1, val2)} \033[37me\033[36m {min(val1, val2)} \033[37mé:\033[33m '
      f'{subt}\n')

print(f'\033[37mA multiplicação entre\033[36m {max(val1, val2)} \033[37me\033[36m {min(val1, val2)} \033[37mé:\033[33m '
      f'{mult}\n')

print(f'\033[37mA divisão entre\033[36m {max(val1, val2)} \033[37me\033[36m {min(val1, val2)} \033[37mé:\033[33m {div}'
      f'\n')


# ------------------------- ↓ recebe N valores e mostra o maior ↓ ----------------------------

print(f"\033[33m{'-' * 90}\n\033[94m{'↓ recebe N valores e mostra o maior ↓'.center(90)}\033[33m\n{'-' * 90}\033[0m")

print(max(4, 67, 54))

print(max('a', 'ab', 'abc'))

print(max('a', 'b', 'c', 'g'))

print(max(3.145, 5.789))

print('O maior valor é: ' + (max('Geek', 'University')))

# ------------------------- ↓ min ↓ ----------------------------

print(f"\033[33m{'-' * 90}\n\033[94m{'↓ recebe N valores e mostra o menor ↓'.center(90)}\033[33m\n{'-' * 90}\033[0m")

print(min(4, 67, 54))

print(min('a', 'ab', 'abc'))

print(min('a', 'b', 'c', 'g'))

print(min(3.145, 5.789))

print('O menor valor é: ' + (min('Geek', 'University')))

# ------------------------- ↓ outros exemplos ↓ ----------------------------

print(f"\033[33m{'-' * 90}\n\033[94m{'↓ outros exemplos ↓'.center(90)}\033[33m\n{'-' * 90}\033[0m")

nomes = ['Ale', 'Aline', 'Júlia', 'Laura', 'Isabella', 'Maria Flor', 'Rapha', 'Gabi']

print(max(nomes))  # Rapha

print(min(nomes))  # Ale

print(max(nomes, key=lambda nome: len(nome)))  # Maria Flor

print(min(nomes, key=lambda nome: len(nome)))  # Ale

# ------------------------- ↓ música que mais tocou e menos tocou ↓ ----------------------------

print(f"\033[33m{'-' * 90}\n\033[94m{'↓ música que mais tocou e menos tocou ↓'.center(90)}\033[33m\n{'-' * 90}\033[0m")

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too Old to Rock 'n' Roll, Too Young to Die", "tocou": 32},
]

print(f'A música mais tocada foi: \033[36m' + max(musicas, key=lambda music: music['tocou'])['titulo'] + '\033[0m'
      + '\033[0m - tocou ' + '\033[36m' + str(max(musicas, key=lambda music: music['tocou'])['tocou']) +
      ' vezes\033[0m')

print(f'A música menos tocada foi: \033[36m' + min(musicas, key=lambda music: music['tocou'])['titulo'] + '\033[0m'
      + '\033[0m - tocou ' + '\033[36m' + str(min(musicas, key=lambda music: music['tocou'])['tocou']) +
      ' vezes\033[0m')

# ------------------------- ↓ música que mais tocou e menos tocou - sem max, min e lambda ↓ ----------------------------

print(f"\033[33m{'-' * 90}\n\033[94m{'↓ música que mais tocou e menos tocou - sem max, min e lambda ↓'.center(90)}"
      f"\033[33m\n{'-' * 90}\033[0m")

maximo = 0
for musica in musicas:
    if musica['tocou'] > maximo:
        maximo = musica['tocou']

for musica in musicas:
    if musica['tocou'] == maximo:
        print(musica['titulo'])

minimo = 9999
for musica in musicas:
    if musica['tocou'] < minimo:
        minimo = musica['tocou']

for musica in musicas:
    if musica['tocou'] == minimo:
        print(musica['titulo'])
