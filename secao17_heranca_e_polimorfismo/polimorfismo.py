#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Polimorfismo

Poli -> Muitas
Morfis -> Formas

OBS: método da classe pai reimplementado na classe filha chama 'sobrescrita de método (Overriding)'

Overriding é a mehor representação de polimorfismo.

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
texto = 'Polimorfismo'
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

console.print("[blue]\nclass Base1:\n    pass\n\n"
              ""
              "[black]class Base2:\n    pass\n\n"
              ""
              "[cyan]class Base3:\n    pass\n\n"
              ""
              "[magenta]class MultiDerivadaDireta(Base1, Base2, Base3):  [white]# herda diretamente de Base1, Base2, "
              "Base3.\n    [magenta]pass\n")


class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self):
        console.print(f'{self._Animal__nome} está comendo...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        console.print(f'{self._Animal__nome} fala wau wau!')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        console.print(f'{self._Animal__nome} fala miau!')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        console.print(f'{self._Animal__nome} fala algo...')


felix = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()
