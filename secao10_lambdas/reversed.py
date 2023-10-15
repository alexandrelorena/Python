"""
Reversed

OBS: NÃO confundir com a função reserve() que estudamos nas listas.

- A função reverse() só funciona em Listas.

A função reversed() funciona com qualquer iterável.

"""
# ------------------------- ↓ Reversed ↓ ----------------------------

print(f"\033[33m{'-' * 90}\n\033[94m{'↓ Reversed ↓'.center(90)}\033[33m\n{'-' * 90}\033[0m")

lista = [1, 2, 3, 4, 5]

# res = reversed(lista)

# print(res)

# print(type(res))

print(f'Tipo: {reversed(lista)}\n')
# <list_reverseiterator object at 0x000001F5FEA47340>

print(f'\033[37mLista normal: \033[34m{list(lista)}\033[36m => {type(lista)}\n\033[0m')
# [1, 2, 3, 4, 5]

print(f'\033[37mLista invertida: \033[34m{list(reversed(lista))}\033[36m => {type(list())}\n\033[0m')
# [5, 4, 3, 2, 1]

print(f'\033[37mTupla invertida: \033[34m{tuple(reversed(lista))}\033[36m => {type(tuple())}\n\033[0m')

print(f'\033[37mConjunto invertido: \033[34m{set(reversed(lista))}\033[36m => {type(set())}\033[0m => set() não '
      f'inverteu pq não define ordem\n')

# ------------------------- ↓ Utilizando o for() ↓ ----------------------------

print(f'\033[37m--------------------------------- ↓ \033[34mUtilizando o for() \033[37m↓ ------------------------------'
      f'---\n\033[0m')

print("Utilizando o for() => ", end='')

for letra in reversed('Geek University'):
    print(letra, end='')

print('\n')

# ------------------------------ ↓ Utilizando o join() ↓ ----------------------------

print(f'\033[37m-------------------------------- ↓ \033[34mUtilizando o join() \033[37m↓ ------------------------------'
      f'---\n\033[0m')

print("Utilizando o join() => ", end='')

print(''.join(list(reversed('Geek University'))))

print()

# ------------------------------ ↓ Utilizando o slice() ↓ ----------------------------

print(f'\033[37m------------------------------- ↓ \033[34mUtilizando o slice() \033[37m↓ ------------------------------'
      f'---\n\033[0m')

print("Utilizando o slice() => ", end='')

print('Geek University'[::-1])

print()

# ------------------------------ ↓ Loop for reverso com reversed() ↓ ----------------------------

print(f'\033[37m-------------------------- ↓ \033[34mLoop for reverso com reversed() \033[37m↓ ------------------------'
      f'---\n\033[0m')

for n in reversed(range(0, 10)):
    if n == 0:  # validando imprimir a vírgula enquanto n != 0
        print(n, end='')
    else:
        print(n, end=',')

print()

# ------------------------------ ↓ Loop for reverso usando o próprio range ↓ ----------------------------

print(f'\033[37m---------------------- ↓ \033[34mLoop for reverso usando o próprio range \033[37m↓ --------------------'
      f'---\n\033[0m')

for n in range(9, -1, -1):
    if n == 0:  # validando imprimir a vírgula enquanto n != 0
        print(n, end='')
    else:
        print(n, end=',')

print()
