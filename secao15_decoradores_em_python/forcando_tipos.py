#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Forçando tipos de dados com Decorators

"""

import shutil
from rich.console import Console
from rich.text import Text
# from functools import wraps
# from rich import print
# from rich.padding import Padding
# from rich.style import Style
# from rich.console import Console
# from rich.table import Table
# from secao08_funcoes.minhas_funcoes import imprimir_com_cores
# from colorama import Fore

# -------------------------------------------- ↓ Bloco título ↓ --------------------------------------------

console = Console()

# Defina a cor do texto e a altura do fundo desejadas
cor_do_texto = "blue"  # Cor do texto (ex: white, red, blue, etc.)
altura_do_fundo = 2  # Altura do fundo em número de linhas

texto = 'Forçando tipos de dados com Decorators'  # Texto a ser exibido

tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

texto_formatado = Text()  # Crie um objeto Text para formatar o texto
texto_formatado.append(texto_centralizado, style=f" black {cor_do_texto}")

for _ in range(altura_do_fundo - 1):  # Adicione quebras de linha para controlar a altura
    largura_terminal = shutil.get_terminal_size().columns
    console.print()
    console.print("[blue]-" * int(0.5 * largura_terminal))
    console.print(texto_formatado.append(""))
    console.print("[blue]-" * int(0.5 * largura_terminal))

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

console.print()

console.print("[cyan]def forca_tipo(*tipos):\n    def decorador(funcao):\n        def converte(*args, **kwargs):\n"
              "            novo_args = []\n            for(valor, tipo) in zip(args, tipos):\n"
              "                novo_args.append(tipo(valor))\n            return funcao(*novo_args, **kwargs)\n"
              "        return converte\n    return decorador\n")


def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):  # args é imutável
            novo_args = []  # gerando um novo args para conversão
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador


console.print("[green]@forca_tipo[/green](str, int)\n[blue]def repet_msg(msg, vezes):\n    for vez in range(vezes):\n"
              "        print(msg)\n")

console.print("repet_msg('Geek', '3')\n")


@forca_tipo(str, int)
def repet_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


repet_msg('Geek', '3')

# ---------------------------------------------------------------------------------------------------------------------

console.print()
console.print(f'[yellow]-' * 90 + f'')
console.print()

console.print("[green]@forca_tipo[/green](float, float)\n[blue]def dividir(a, b):\n    print(a/b)\n")

console.print("dividir(1, 5)\n")


@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)


dividir(1, 5)
