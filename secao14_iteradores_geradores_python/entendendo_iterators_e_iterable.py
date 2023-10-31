"""
Entendendo Iterators e Iterables

Iterator ->
    - Um objeto que pode ser iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada.

Iterable ->
    - Um objeto que irá retornar um iterator quando a função iter() for chamada.

"""


from colorama import Fore, Back, init
"""import os
# import platform
# import sys
import shutil
from send2trash import send2trash
import tempfile"""

# -------------------------------------------- ↓ Bloco título ↓ --------------------------------------------

# Inicialize o Colorama

init(autoreset=True)

# Cor de fundo que você deseja
cor_de_fundo = Back.BLUE

# Altura do fundo (número de linhas)
altura_do_fundo = 1

# Largura da linha
largura_da_linha = 145

# Imprime as linhas de início com a cor amarela
print(f"{Fore.BLACK}{'-' * 145}\033[0m")

# Imprime o fundo com a altura desejada
[print(cor_de_fundo + ' ' * largura_da_linha) for _ in range(altura_do_fundo)]

# Texto que você quer em preto
texto = 'Entendendo Iterators e Iterables'

# Imprime o texto "Bloco with" em preto no meio do fundo amarelo
print(Fore.BLACK + cor_de_fundo + texto.center(largura_da_linha))

# Imprime o fundo novamente com a altura desejada
[print(cor_de_fundo + ' ' * largura_da_linha) for _ in range(altura_do_fundo)]

# Imprime as linhas de término com a cor amarela
print(f"{Fore.BLACK}{'-' * 145}\033[0m")

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

print(Fore.CYAN + f"{'↓ Iterables ↓'.center(145)}\n"f"{Fore.CYAN}{'-' * 145}\033[0m"
                  f"\n")

# Iterables
nome = 'Geek'
numeros = [1, 2, 3, 4, 5, 6]

it1 = iter(nome)
it2 = iter(numeros)

print(Fore.YELLOW + "print(next(it1)) " + Fore.LIGHTRED_EX + f'{next(it1)}')
print(Fore.YELLOW + "print(next(it1)) " + Fore.LIGHTRED_EX + f'{next(it1)}')
print(Fore.YELLOW + "print(next(it1)) " + Fore.LIGHTRED_EX + f'{next(it1)}')
print(Fore.YELLOW + "print(next(it1)) " + Fore.LIGHTRED_EX + f'{next(it1)}')

# print(next(it1))  # se tentar iterar na string mais vezes que o numero de caracteres, dá erro StopIteration.
print()

print(Fore.LIGHTBLUE_EX + "print(next(it1)) " + Fore.LIGHTYELLOW_EX + f'{next(it2)}')
print(Fore.LIGHTBLUE_EX + "print(next(it1)) " + Fore.LIGHTYELLOW_EX + f'{next(it2)}')
print(Fore.LIGHTBLUE_EX + "print(next(it1)) " + Fore.LIGHTYELLOW_EX + f'{next(it2)}')
print(Fore.LIGHTBLUE_EX + "print(next(it1)) " + Fore.LIGHTYELLOW_EX + f'{next(it2)}')
print(Fore.LIGHTBLUE_EX + "print(next(it1)) " + Fore.LIGHTYELLOW_EX + f'{next(it2)}')
print(Fore.LIGHTBLUE_EX + "print(next(it1)) " + Fore.LIGHTYELLOW_EX + f'{next(it2)}')

# por baixo dos panos
print()

print("É a mesma coisa que:" + Fore.MAGENTA + "\nfor letra in nome:\n    print(f'{letra}') ")

for letra in nome:
    print(Fore.BLACK + f'{letra}')
