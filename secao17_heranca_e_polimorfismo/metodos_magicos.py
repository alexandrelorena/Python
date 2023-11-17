#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POO - Métodos mágicos

São todos os métodos que utilizam dunder -> Double underscore

- dunder init: __init__()
- dunder repr: __repr__() -> representação do objeto



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
texto = 'POO - Métodos mágicos'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

texto = 'Usando __repr__() >> com a representação do objeto'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("[blue]\nclass Livro:\n\n    def __init__(self, titulo, autor, paginas):\n"
              ""
              "[black]        self.titulo = titulo\n"
              ""
              "[cyan]        self.autor = autor\n"
              ""
              "[magenta]        self.paginas = paginas\n\n"
              ""
              "    [black]def __repr__(self):  [white]# __repr__() tem a função de fazer a representção do objeto.\n"
              "    [black]pass"
              "\n"
              ""
              "        return f'[blue]{self.titulo} [green]escrito por [blue]{self.autor}'\n\n")


console.print("livro1 = Livro('Python Rocks','Geek University',400)")
console.print("livro2 = Livro('Inteligência Artificial com Python','Geek University', 350)")

console.print()

console.print("console.print(f'{livro1}')")
console.print("console.print(f'{livro2}')")


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):  # __repr__() tem a função de fazer a representção do objeto.
        return f'[blue]{self.titulo} [green]escrito por [blue]{self.autor}'


livro1 = Livro('Python Rocks', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)

console.print()

console.print(f'{livro1}')
console.print(f'{livro2}')

# ---------------------------------------------------------------------------------------------------------------------

texto = 'Sem usar __repr__() >> mostra o endereço de memória'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("[blue]\nclass Livro:\n\n    def __init__(self, titulo, autor, paginas):\n"
              ""
              "[black]        self.titulo = titulo\n"
              ""
              "[cyan]        self.autor = autor\n"
              ""
              "[magenta]        self.paginas = paginas\n"
              "")


livro1 = Livro('Python Rocks', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)


console.print("console.print(f'{livro3}')")
console.print("console.print(f'{livro4}')")


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


livro3 = Livro('Python Rocks', 'Geek University', 400)
livro4 = Livro('Inteligência Artificial com Python', 'Geek University', 350)

console.print()

console.print(f'[yellow]{livro3}')
console.print(f'[blue]{livro4}')
