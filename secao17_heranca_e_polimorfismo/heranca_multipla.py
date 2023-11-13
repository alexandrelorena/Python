#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POO - Heranca Múltipla

- Nada mais é do que a possibilidade de uma classe herdar de múltiplas classes.
    - Multiderivação direta;
    - Multiderivação indireta;


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
texto = 'POO - Heranca Múltipla'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

texto = 'Multiderivação Direta'
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


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivadaDireta(Base1, Base2, Base3):  # herda diretamente de Base1, Base2, Base3.
    pass


# ---------------------------------------------------------------------------------------------------------------------


texto = 'Multiderivação Indireta'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("[blue]\nclass Base1:\n    pass\n\n"
              ""
              "[white]class Base2[blue](Base1):\n    pass\n\n"
              ""
              "[cyan]class Base3[white](Base2):\n    pass\n\n"
              ""
              "[magenta]class MultiDerivadaIndireta[cyan](Base3):  [white]# herda diretaamente de Base3 e indiretamente"
              " de Base1 e Base2.\n    [magenta]pass\n")


class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerivadaIndireta(Base3):  # herda diretaamente de Base3 e indiretamente de Base1 e Base2.
    pass


# ---------------------------------------------------------------------------------------------------------------------

texto = 'Exemplo prático'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("\n[blue]class Animal:\n\n    def __init__(self, nome):\n        self.__nome = nome\n\n"
              ""
              "    [black]def cumprimentar(self):\n        return f'Eu sou {self.__nome}'\n\n"
              ""
              "[cyan]class Aquatico(Animal):\n\n    def __init__(self, nome):\n        super().__init__(nome)\n\n"
              ""
              "    [magenta]def nadar(self):\n        return f'{self._Animal__nome} está nadando!'\n\n"
              ""
              "    [blue]def cumprimentar(self):\n        return f'Eu sou um {self._Animal__nome} marinho'\n\n"
              ""
              "[black]class Terrestre(Animal):\n\n    def __init__(self, nome):\n        super().__init__(nome)\n\n"
              ""
              "    [cyan]def andar(self):\n        return f'{self._Animal__nome} está andando!'\n\n"
              ""
              "    [magenta]def cumprimentar(self):\n        return f'Eu sou um {self._Animal__nome} da terra!'\n\n"
              ""
              "[blue]class Pinguim(Aquatico, Terrestre):\n\n    def __init__(self, nome):\n    def __init__(self, nome)"
              ":\n")


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
        return f'Eu sou um {self._Animal__nome} marinho!'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando!'

    def cumprimentar(self):
        return f'Eu sou um {self._Animal__nome} da terra!'


class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)


console.print("baleia = Aquatico('Wally')")
console.print("console.print(baleia.nadar())")
console.print("console.print(baleia.cumprimentar())")

console.print()

baleia = Aquatico('Wally')
console.print(baleia.nadar())
console.print(baleia.cumprimentar())

console.print()

console.print("tatu = Terrestre('Xim')")
console.print("console.print(tatu.andar())")
console.print("console.print(tatu.cumprimentar())")

console.print()

tatu = Terrestre('Xim')
console.print(tatu.andar())
console.print(tatu.cumprimentar())

console.print()

console.print("tux = Pinguim('Tux')")
console.print("console.print(tux.andar())")
console.print("console.print(tux.nadar())")
console.print("console.print(tux.cumprimentar())"
              "[white]# ??? Methodo Resolution Order - MRO  => print dependerá da ordem da herança na classe Pinguim")

console.print()

tux = Pinguim('Tux')
console.print(tux.andar())
console.print(tux.nadar())
console.print(tux.cumprimentar())
# ??? Methodo Resolution Order - MRO  => print dependerá da ordem da herança na classe Pinguim

console.print()

console.print("[cyan]console.print(f'Tux é instância de Pinguim? {isinstance(tux, Pinguim)}')  [white]# True")
console.print(f'[blue]Tux é instância de Pinguim? {isinstance(tux, Pinguim)}')  # True

console.print()

console.print("[cyan]console.print(f'Tux é instância de Aquático? {isinstance(tux, Aquático)}')  [white]# True")
console.print(f'[yellow]Tux é instância de Aquático? {isinstance(tux, Aquatico)}')  # True
console.print()

console.print("[cyan]console.print(f'Tux é instância de Terrestre? {isinstance(tux, Terrestre)}')  [white]# True")
console.print(f'[magenta]Tux é instância de Terrestre? {isinstance(tux, Terrestre)}')  # True
console.print()

console.print("[cyan]console.print(f'Tux é instância de Animal? {isinstance(tux, Animal)}')  [white]# True")
console.print(f'[black]Tux é instância de Animal? {isinstance(tux, Animal)}')  # True
console.print()

console.print("[cyan]console.print(f'Tux é instância de object? {isinstance(tux, object)}')  [white]# True")
console.print(f'[white]Tux é instância de object? {isinstance(tux, object)}')  # True
