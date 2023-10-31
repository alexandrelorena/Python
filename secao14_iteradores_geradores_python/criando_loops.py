"""
Criando sua própria versão de loop



"""

from colorama import Fore, Back, init
from termcolor import colored

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
texto = 'Criando Loopss'

# Imprime o texto "Bloco with" em preto no meio do fundo amarelo
print(Fore.BLACK + cor_de_fundo + texto.center(largura_da_linha))

# Imprime o fundo novamente com a altura desejada
[print(cor_de_fundo + ' ' * largura_da_linha) for _ in range(altura_do_fundo)]

# Imprime as linhas de término com a cor escolhida
print(f"{Fore.BLACK}{'-' * 145}\033[0m")

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

print(f"{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ meu_for - opção 1 ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")


def meu_for(iteravel):
    it = iter(iteravel)
    try:
        element = next(it)
        while True:
            try:
                next_element = next(it)
                if element != ' ' and next_element != ' ':
                    # Imprimir o elemento e um pipe, a menos que seja um espaço
                    print(element, end=' | ')
                else:
                    # Não imprimir pipe se for um espaço
                    print(element, end=' ')
                element = next_element
            except StopIteration:
                break
        # Imprimir o último elemento
        print(element)
    except StopIteration:
        pass


meu_for(list('Geek University'))
print()

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

meu_for(numeros)
print()

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ meu_for - opção 2 ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")


def imprimir_com_cores(iteravel):
    cores = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    estilos = ['bold', 'underline', 'blink']  # Exemplos de estilos
    cor_index = 0
    estilo_index = 0

    for letra in iteravel:
        if letra != ' ':
            cor = cores[cor_index % len(cores)]
            estilo = estilos[estilo_index % len(estilos)]  # Use o estilo atual
            letra_colorida = colored(letra, cor, attrs=[estilo])  # Passar o estilo
            print(letra_colorida, end=' ')
            cor_index += 1
            estilo_index += 1
        else:
            print(letra, end=' ')

    print()  # Pular uma linha após a impressão


imprimir_com_cores('Brasil')

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ meu_for - opção 3 ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")


def imprimir_com_cores(iteravel):
    cores = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    cor_index = 0

    nome_atual = ''
    nomes = []

    for letra in iteravel:
        if letra != ' ':
            cor = cores[cor_index % len(cores)]
            letra_colorida = colored(letra, cor)
            nome_atual += letra_colorida
            cor_index += 2
        else:
            nomes.append(nome_atual)
            nome_atual = ''

    # Verifica se há um nome atual a ser adicionado à lista
    if nome_atual:
        nomes.append(nome_atual)

    # Imprimir os nomes juntos com um espaço entre eles
    print(' '.join(nomes))


imprimir_com_cores('Santos Futebol Clube')

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ meu_for - opção 4 ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")


def imprimir_com_cores(iteravel):
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

    print(nome_atual)  # Imprimir o último nome


imprimir_com_cores('Alexandre Lorena')


# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ meu_for - opção 5 ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")


def meu_for(iteravel):
    cores = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    cor_index = 0
    it = iter(iteravel)
    try:
        element = next(it)
        while True:
            try:
                next_element = next(it)
                if element != ' ' and next_element != ' ':
                    cor = cores[cor_index % len(cores)]
                    element_colorido = colored(element, cor)
                    # Imprimir o elemento colorido e um pipe, a menos que seja um espaço
                    print(element_colorido, end=' | ')
                    cor_index += 1
                else:
                    # Não imprimir pipe se for um espaço
                    print(element, end=' ')
                element = next_element
            except StopIteration:
                break
        # Imprimir o último elemento
        cor = cores[cor_index % len(cores)]
        element_colorido = colored(element, cor)
        print(element_colorido)
    except StopIteration:
        pass


meu_for(list('Alexandre Lorena'))
