#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POO - Classes

Classes podem conter:
    - Atributos -> representam as características do objeto
    - Métodos (funções) -> representam o comportamento do objeto

Nossas classes, por convenção são criadas com inicial maiúscula, inclusive nome composto (ex: ContaCorrente)

OBS: Classes internas do Python tem a inicial minúscula.

OBS2: Em planejamento de software, quando são definidas as classes que farão parte do sistema, chamamos
essas classes de 'ENTIDADES'.

"""

# import shutil
from rich.console import Console
# from rich.text import Text
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

texto = 'POO - classes'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[on yellow][bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

# console.print()
console.print("[green]class [black]Lampada:\n    [green]pass\n")

#  Utilizamos a palavra reservada 'class' para criar uma classe. A palavra pass é utilizada
#  quando temos um código que ainda não foi implementado.


class Lampada:
    pass


console.print("[cyan]lamp = Lampada()")
lamp = Lampada()

console.print("[cyan]console.print(type(lamp)) => ", end='')
console.print(type(lamp))


class ContaCorrente:
    pass


class Produto:
    pass


class Usuario:
    pass


console.print(f'[white]-' * 90 + f'')
