#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Método super()

- Se refere á super classe.
"""
from rich.console import Console
# import shutil
# from rich.text import Text
# from functools import wraps
# from rich import print
# from rich.terminal_theme import TerminalTheme
# from rich.padding import Padding
# from rich.style import Style
# from rich.console import Console
# from rich.table import Table
# from secao08_funcoes.minhas_funcoes import imprimir_com_cores
# from colorama import Fore
# from passlib.hash import pbkdf2_sha256 as cryp

# -------------------------------------------- ↓ Bloco título ↓ --------------------------------------------

console = Console()

console.print()
texto = 'POO - Método super()'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

texto = ''
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
# console.print(f'[bold white][center]' + texto_centralizado)
# console.print(f'[yellow]-' * 90)

console.print("[blue]class Animal:\n\n    def __init__(self, nome, especie):\n        self.__nome = nome\n        "
              "self.__especie = especie\n\n"
              ""
              "    def faz_som(self, som):\n        print(f'O {self.__nome} faz {som}')\n\n"
              ""
              "[black]class Gato(Animal):\n    def __init__(self, nome, especie, raca):\n        "
              "super().__init__(nome, especie)\n        super().faz_som('auahauahu')\n        self.__raca = raca\n")


class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} faz {som}')


class Gato(Animal):

    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie)
        super().__init__(nome, especie)
        super().faz_som('auahauahu')
        self.__raca = raca


console.print("felix = Gato('Felix', 'Felino', 'Angorá')")

console.print("felix.faz_som('miau')")

console.print()

felix = Gato('Felix', 'Felino', 'Angorá')

felix.faz_som('miau')
