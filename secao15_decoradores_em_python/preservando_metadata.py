#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Preservando Metadata com Wraps

Metadados -> são dados intrínsecos em arquivos

wraps -> são funções que envolvem elementos com diversas finalidades

"""
import shutil
from rich.console import Console
from rich.text import Text
from functools import wraps
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
cor_do_texto = "black"  # Cor do texto (ex: white, red, blue, etc.)
altura_do_fundo = 2  # Altura do fundo em número de linhas

texto = 'Preservando Metadata com Wraps'  # Texto a ser exibido

tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

texto_formatado = Text()  # Crie um objeto Text para formatar o texto
texto_formatado.append(texto_centralizado, style=f"on black {cor_do_texto}")

for _ in range(altura_do_fundo - 1):  # Adicione quebras de linha para controlar a altura
    largura_terminal = shutil.get_terminal_size().columns
    console.print()
    console.print("[on blue] " * int(0.5 * largura_terminal))
    console.print(texto_formatado.append(""))
    console.print("[on blue] " * int(0.5 * largura_terminal))

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------


def ver_log(funcao):
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra!"""
        console.print(f'[green]Você está chamando [cyan]{funcao.__name__}')
        console.print(f'[green]Documentação:[cyan]{funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b


console.print()
console.print(f'[blue]O resultado da soma é: {soma(10, 30)}')
console.print()

# ---------------------------------------------------------------------------------------------------------------------
# problema:
console.print(f'[yellow]-' * 90 + f'')
console.print()
console.print(f'[red]Problema! [bold red]Não trouxe a documentação correta =>>[red] {soma.__name__}')
console.print(f'[green]Documentação:[cyan]{soma.__doc__}')
console.print()

console.print(f'[yellow]-' * 90 + f'')

# ---------------------------------------------------------------------------------------------------------------------

# resolução do problema:


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) de ntro de outra"""
        console.print(f'[green]Você está chamando [cyan]{funcao.__name__}')
        console.print(f'[green]Documentação:[cyan]{funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b


console.print()
console.print(f'[black]Com [cyan]"wraps"[/cyan] você está chamando corretamente a documentação: [blue]{soma.__name__}')
console.print(f'[green]Documentação: [cyan]{soma.__doc__}')
console.print()
console.print(f'[yellow]-' * 90 + f'')
console.print()
console.print(soma(10, 30))
