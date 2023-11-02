"""
Teste de memória com Generators

# Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13...
"""
from colorama import Fore, Back, init
# from termcolor import colored

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

# Imprime as linhas de início com a cor escolhida
print(f"{Fore.BLACK}{'-' * 145}\033[0m")

# Imprime o fundo com a altura desejada
[print(cor_de_fundo + ' ' * largura_da_linha) for _ in range(altura_do_fundo)]

# Texto que você quer em preto
texto = 'Teste de memória com Generators'

# Imprime o texto "Bloco with" em preto no meio do fundo amarelo
print(Fore.BLACK + cor_de_fundo + texto.center(largura_da_linha))

# Imprime o fundo novamente com a altura desejada
[print(cor_de_fundo + ' ' * largura_da_linha) for _ in range(altura_do_fundo)]

# Imprime as linhas de término com a cor escolhida
print(f"{Fore.BLACK}{'-' * 145}\033[0m")

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

print(f"{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Function usando listas - consomem mais memória ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

print(Fore.MAGENTA + "def fib_lista(max): \n    nums = []\n    a, b = 0, 1\n    while len(nums) < max:\n        "
                     "nums.append(b)\n        a, b = b, a + b\n    return nums")

print()

print(Fore.BLUE + "print(fib_lista(10))")

print()


def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


print(fib_lista(10))

print()

print(Fore.BLUE + "print(fib_lista(100))")

print()

print(Fore.LIGHTYELLOW_EX + f'{fib_lista(100)}')

print()

print(Fore.MAGENTA + "for n in fib_lista(100):\n    print(Fore.LIGHTBLUE_EX + f'{n}')")

print()

for n in fib_lista(100):
    print(Fore.LIGHTBLUE_EX + f'{n}')

print()

print(f"{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Generator Function - consome menos memória que listas ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")


print(Fore.MAGENTA + "def fib_gen(max):\n    a, b, contador = 0, 1, 0\n    while contador < max:\n        "
                     "a, b = b, a + b\n        yield a\n        contador = contador + 1")

print()

print(Fore.BLUE + "print(fib_gen(100))")

print()


def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


print(list(fib_gen(100)))

print()

print(Fore.MAGENTA + "for n in fib_gen(100):\n    print(Fore.LIGHTYELLOW_EX + f'{n}')")

print()

for n in fib_gen(100):
    print(Fore.LIGHTYELLOW_EX + f'{n}')
