"""
Geradores

- geradores (Generators) são Iterators (Iteradores)

OBS:
    - Nem todo Iterator é um Generator;
    - Funções geradoras utilizam a palavra reservada yield;
    - Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions

----------------------------------------------------------------
/ Funções                            / Generator Functions     /
----------------------------------------------------------------
/ Utilizam returned                  / utilizam yield          /
----------------------------------------------------------------
/ retorna uma vez                    / pode usar yield n vezes /
----------------------------------------------------------------
/ quando executada, retorna um valor / retorna um generator    /
----------------------------------------------------------------

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
texto = 'Geradores'

# Imprime o texto "Bloco with" em preto no meio do fundo amarelo
print(Fore.BLACK + cor_de_fundo + texto.center(largura_da_linha))

# Imprime o fundo novamente com a altura desejada
[print(cor_de_fundo + ' ' * largura_da_linha) for _ in range(altura_do_fundo)]

# Imprime as linhas de término com a cor escolhida
print(f"{Fore.BLACK}{'-' * 145}\033[0m")

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

print(f"{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Generator Function ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

print(Fore.MAGENTA + "def conta_ate(valor_maximo): \n    contador = 1\n    while contador <= valor_maximo:\n        "
                     "yield contador\n""        contador += 1")


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1  # contador = contador + 1

# OBS: Uma Generator Function não é um Generator. Ela gera um Generator.


print()

print("gen = conta_ate(5)")

print()

print("print(type(gen))")

print()

print(f"{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ gen = conta_ate(5) ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

gen = conta_ate(5)

print(f'print(type(gen) -> {type(gen)}')

print()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ gen = conta_ate(10) ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

gen = conta_ate(10)

print(next(gen))  # imprime 1

print()

for num in gen:
    print(num)  # continua a partir do 2 -> yield fica aguardando o resto da utilização.

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ gen = list(conta_ate(10)) ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

gen = list(conta_ate(10))

print(gen)
