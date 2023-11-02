"""
Teste de velocidade com expressões geradoras

"""
from colorama import Fore, Back, init
# from termcolor import colored
import time

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
texto = 'Teste de velocidade com expressões geradoras'

# Imprime o texto "Bloco with" em preto no meio do fundo amarelo
print(Fore.BLACK + cor_de_fundo + texto.center(largura_da_linha))

# Imprime o fundo novamente com a altura desejada
[print(cor_de_fundo + ' ' * largura_da_linha) for _ in range(altura_do_fundo)]

# Imprime as linhas de término com a cor escolhida
print(f"{Fore.BLACK}{'-' * 145}\033[0m")

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

print(f"{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Generator ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

print(Fore.MAGENTA + "def nums():\n    for num in range(1, 10):\n        yield num\n")
print(Fore.YELLOW + "print(g1)  # Generator\nprint(next(g1))\nprint(next(g1))\n")

#  Generators (Geradores)


def nums():
    for num in range(1, 10):
        yield num


g1 = nums()

print(Fore.LIGHTBLUE_EX + f'{g1}')  # Generator

print(next(g1))
print(next(g1))

print(f"{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Generator Expression ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

print(Fore.MAGENTA + "ge2 = (num for num in range(1, 10))\n")
print(Fore.YELLOW + "print(ge2)  # Generator Expression\nprint(next(g2))\nprint(next(g2))\n")

#  Generator Expression

ge2 = (num for num in range(1, 10))

print(Fore.BLUE + f'{ge2}')  # Generator Expression

print(next(ge2))
print(next(ge2))

print(f"{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Generator Expression X List Comprehension ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m")

# Realizando o teste de velocidade
print(Fore.BLUE + f" ↓ Generator Expression ↓".center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

#  Generator Expression
print(Fore.MAGENTA + "gen_inicio = time.time()\n")
print(Fore.YELLOW + "print(sum(num for num in range(100000000)))  # 100 milhôes\n")
print(Fore.CYAN + "gen_tempo = time.time() - gen_inicio\n")

gen_inicio = time.time()
print(sum(num for num in range(100000000)))  # 100 milhôes
gen_tempo = time.time() - gen_inicio

print()
print(Fore.YELLOW + "print(Fore.BLUE + f'Generator Expression levou {gen_tempo}')\n")
print(Fore.BLUE + f'Generator Expression levou {gen_tempo}')

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.BLUE} ↓ List Comprehension ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")
#  List Comprehension
print(Fore.MAGENTA + "list_inicio = time.time()\n")
print(Fore.YELLOW + "print(sum([num for num in range(100000000)]))\n")
print(Fore.CYAN + "list_tempo = time.time() - list_inicio\n")

list_inicio = time.time()
print(sum([num for num in range(100000000)]))  # 100 milhôes
list_tempo = time.time() - list_inicio

print()
print(Fore.YELLOW + "print(Fore.MAGENTA + f'List Comprehension levou {list_tempo}')\n")
print(Fore.BLUE + f'List Comprehension levou {list_tempo}')
