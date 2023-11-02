from colorama import Fore, Back, init
from random import choice
from secao08_funcoes.minhas_funcoes import imprimir_com_cores
"""
Funções de maior grandeza - Higher Order Functions - HOF

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções
que rettornam outras funçõs como resultado.

- HOF são funções que retornam outras funções.

- Em Python, as Funções são First Class Citzen (Cidadãos de primeira classe)
"""
"""import sys
sys.path.append('/..secao08_funcoes')
"""

# from termcolor import colored
# import time
# import os
# import platform
# import sys
# import shutil
# from send2trash import send2trash
# import tempfile

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
texto = 'Funções de maior grandeza'

# Imprime o texto "Bloco with" em preto no meio do fundo amarelo
print(Fore.BLACK + cor_de_fundo + texto.center(largura_da_linha))

# Imprime o fundo novamente com a altura desejada
[print(cor_de_fundo + ' ' * largura_da_linha) for _ in range(altura_do_fundo)]

# Imprime as linhas de término com a cor escolhida
print(f"{Fore.BLACK}{'-' * 145}\033[0m")

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

print(Fore.BLUE + f"↓ Definindo as Funções ↓".center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

print(Fore.MAGENTA + "def somar(a, b):\n     return a + b\n\ndef diminuir(a, b):\n    return a - b\n\n"
                     "def multiplicar(a, b):\n    return a * b\n\ndef dividir(a, b):\n    return a / b\n")

print(Fore.YELLOW + "print(f'A soma: 4 + 3 = {calcular(4, 3, somar)}')")
print(Fore.CYAN + "print(f'A subtração: 4 - 3 = {calcular(4, 3, diminuir)}')")
print(Fore.BLUE + "print(f'A multiplicação: 4 * 3 = {calcular(4, 3, multiplicar)}')")
print(Fore.LIGHTCYAN_EX + "print(f'A divisão: 4 / 3 = {calcular(4, 3, dividir)}')")


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


print()

print(Fore.YELLOW + f'A soma: 4 + 3 = {calcular(4, 3, somar)}')

print(Fore.CYAN + f'A subtração: 4 - 3 = {calcular(4, 3, diminuir)}')

print(Fore.BLUE + f'A multiplicação: 4 * 3 = {calcular(4, 3, multiplicar)}')

print(Fore.LIGHTCYAN_EX + f'A divisão: 4 / 3 = {calcular(4, 3, dividir)}')

# ---------------------------------------------------------------------------------------------------------------------

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Nested Function - Funções Aninhadas - função dentro da função ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

print(Fore.MAGENTA + "def cumprimento(pessoa):\n    def humor():\n        return choice(('E aí', 'Suma daqui', 'Gosto "
                     "muito de você'))\n    return humor() + pessoa")

print(Fore.CYAN + "\nprint(cumprimento(' Angelina'))")
print(Fore.YELLOW + "print(cumprimento(' Felicity'))\n")


def cumprimento(pessoa):
    def humor():
        return choice(('E aí', 'Suma daqui', 'Gosto muito de você'))
    return humor() + pessoa


print(Fore.CYAN + f'{cumprimento(" Angelina")}')

print(Fore.YELLOW + f'{cumprimento(" Felicity")}')

# ---------------------------------------------------------------------------------------------------------------------

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Retornando Funções de outras Funções ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

print(Fore.MAGENTA + "def faz_me_rir():\n    def rir():\n        return choice(('hahahahahahaha','kkkkkkkkkkkk', "
                     "'uahauhauhauahuah'))\n    return rir")

print(Fore.CYAN + "\nrindo = faz_me_rir()")
print(Fore.YELLOW + "print(rindo())\n")


def faz_me_rir():
    def rir():
        return choice(('hahahahahahaha','kkkkkkkkkkkk', 'uahauhauhauahuah', 'ushushus uhuahauhau'))
    return rir


rindo = faz_me_rir()

# imprimindo colorido a função rir


"""def imprimir_com_cores(iteravel):
    cores = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    cor_index = 0

    nome_atual = ''

    for letra in iteravel:
        if letra != ' ':
            cor = cores[cor_index % len(cores)]
            letra_colorida = colored(letra, cor)
            nome_atual += letra_colorida
            cor_index += 2
        else:
            print(nome_atual, end=' ')
            nome_atual = ''

    print(nome_atual)  # Imprimir o último nome"""


texto_colorido = rindo()  # Obter o texto colorido de rindo
imprimir_com_cores(texto_colorido)  # Imprimir o texto colorido

# ---------------------------------------------------------------------------------------------------------------------

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Inner Functions ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

print(Fore.MAGENTA + "def faz_me_rir_novamente(pessoa):\n    def dando_risada():\n        risada = choice(('hahahahahah"
                     "aha','kkkkkkkkkkkk', 'uahauhauhauahuah', 'ushushus uhuahauhau'))"
                     "        return f'{risada} {pessoa}'\n    return dando_risadar")

print(Fore.CYAN + "\nrindo = faz_me_rir_novamente('Fernanda')")
print(Fore.YELLOW + "print(rindo())\n")


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahahahaha','kkkkkkkkkkkk', 'uahauhauhauahuah', 'ushushus uhuahauhau'))
        return f'{risada} {pessoa}'
    return dando_risada


rindo = faz_me_rir_novamente('Fernanda')

texto_colorido = rindo()  # Obter o texto colorido de rindo
imprimir_com_cores(texto_colorido)  # Imprimir o texto colorido
