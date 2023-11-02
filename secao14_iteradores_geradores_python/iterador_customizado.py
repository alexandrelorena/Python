"""
Escrevendo um Iterador Customizado


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
texto = 'Iterador Customizado'

# Imprime o texto "Bloco with" em preto no meio do fundo amarelo
print(Fore.BLACK + cor_de_fundo + texto.center(largura_da_linha))

# Imprime o fundo novamente com a altura desejada
[print(cor_de_fundo + ' ' * largura_da_linha) for _ in range(altura_do_fundo)]

# Imprime as linhas de término com a cor escolhida
print(f"{Fore.BLACK}{'-' * 145}\033[0m")

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

print(f"{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Criando iterador Customizado ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")


"""for n in range(11):
    print(n)"""

print(Fore.MAGENTA + "class Contador:\n    def __init__(self, menor, maior):\n        self.menor = menor\n   "
                     "     self.maior = maior\n\n    def __iter__(self):\n        return self\n\n"
                     "    def __next__(self):""\n        if self.menor < self.maior:\n""            numero = self.menor"
                     "\n ""           self.menor = self.menor + 1\n            return numero\n        "
                     "raise StopIteration\n\n "" con = Contador(1, 6)\n\n  it = iter(con)\n\n  print(next(it))\n  "
                     "print(next(it))\n  print(next(it))""\n  print(next(it))\n  print(next(it))\n  print(next(it))\n ")


class Contador:
    def __init__(self, menor, maior):  # função dentro de uma classe: método construtor '__init__'
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


con = Contador(1, 6)

it = iter(con)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# ---------------------------------------------------------------------------------------------------------------------


print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ for n in Contador(1, 6): ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

print(Fore.MAGENTA + "for n in Contador(1, 6):\n    print(n)")

for n in Contador(1, 6):
    print(n)

# ---------------------------------------------------------------------------------------------------------------------

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ for n in range(1, 6): ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

print(Fore.MAGENTA + "for n in range(1, 6):\n    print(n)")

for n in range(1, 6):
    print(n)
