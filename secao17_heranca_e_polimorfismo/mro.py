#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
MRO - Method Resolution Order
    É a ordem de execução dos métodos quem será executado primeiro).

Maneiras de conferir a ordem de execução:

    1 - Via propriedade da classe __mro__

        from secao17_heranca_e_polimorfismo.mro import Pinguim
        Pinguim.__mro__
          (<class 'secao17_heranca_e_polimorfismo.mro.Pinguim'>, <class 'secao17_heranca_e_polimorfismo.mro.Terrestre'>,
          <class 'secao17_heranca_e_polimorfismo.mro.Aquatico'>, <class 'secao17_heranca_e_polimorfismo.mro.Animal'>,
          <class 'object'>)

    2 - Via método mro()

        Pinguim.mro()
          (<class 'secao17_heranca_e_polimorfismo.mro.Pinguim'>, <class 'secao17_heranca_e_polimorfismo.mro.Terrestre'>,
          <class 'secao17_heranca_e_polimorfismo.mro.Aquatico'>, <class 'secao17_heranca_e_polimorfismo.mro.Animal'>,
          <class 'object'>)

    3 - Via help

        help(Pinguim)
          Method resolution order:
          Pinguim
          Terrestre
          Aquatico
          Animal
          builtins.object


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
texto = 'MRO - Method Resolution Order'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

texto = ''
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("[blue]\nclass Base1:\n    pass\n\n"
              ""
              "[black]class Base2:\n    pass\n\n"
              ""
              "[cyan]class Base3:\n    pass\n\n"
              ""
              "[magenta]class MultiDerivadaDireta(Base1, Base2, Base3):  [white]# herda diretamente de Base1, Base2, "
              "Base3.\n    [magenta]pass\n")


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando!'

    def cumprimentar(self):
        return f'Eu sou um {self._Animal__nome} do mar!'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando!'

    def cumprimentar(self):
        return f'Eu sou um {self._Animal__nome} da terra!'


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)


console.print()

console.print("tux = Pinguim('Tux')")
console.print("console.print(tux.cumprimentar())"
              "[white]# ??? Methodo Resolution Order - MRO  => print dependerá da ordem da herança na classe Pinguim")

console.print()

tux = Pinguim('Tux')
console.print(tux.cumprimentar())

"""
Pinguim(Aquatico, Terrestre)
Eu sou um Tux do mar!

Pinguim(Terrestre, Aquatico)
Eu sou um Tux da terra!

"""

# ---------------------------------------------------------------------------------------------------------------------
