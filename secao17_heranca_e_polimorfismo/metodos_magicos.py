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
console.print(f'[bold green][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("[blue]\nclass Livro:\n\n    def __init__(self, titulo, autor, paginas):\n"
              ""
              "[black]        self.titulo = titulo\n"
              ""
              "[cyan]        self.autor = autor\n"
              ""
              "[magenta]        self.paginas = paginas\n\n"
              ""
              "[yellow]Com método dunder __repr__()\n\n"
              ""
              "    [black]def __repr__(self):  [white]# __repr__() tem a função de fazer a representção do objeto.\n"
              "    [black]pass"
              "\n"
              ""
              "        return f'[blue]{self.titulo} [green]escrito por [blue]{self.autor}'\n\n"
              ""
              "[yellow]Com método dunder __str__()  [white]# este método tem preferência ao dunder __init__().")

console.print()

console.print("[black]    def __str__(self):\n        return self.titulo\n")

console.print("livro1 = Livro('Python Rocks','Geek University',400)")
console.print("livro2 = Livro('Inteligência Artificial com Python','Geek University', 350)")

console.print()

console.print("[cyan]console.print(f'{livro1}')")
console.print("[cyan]console.print(f'{livro2}')")


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # def __repr__(self):  # __repr__() tem a função de fazer a representção do objeto.
    #     return f'[black]{self.titulo} [white]escrito por [black]{self.autor}'

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('Um objeto do tipo Livro foi deletado da memória!')
        # se usar biblioteca externa rich(console.print()), dará o erro: ImportError: sys.meta_path is None, Python is
        # likely shutting down.

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            separador = ' | '  # Adicionando um separador
            for n in range(outro):
                msg += f'{self}{separador}'  # o self é o próprio objeto
            return msg.rstrip(separador)  # Removendo o último separador antes de retornar
        return 'Não posso multiplicar'


livro1 = Livro('Python Rocks', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial', 'Geek University', 350)
livro3 = Livro('Rocks Artificial', 'Geek University', 200)
livro4 = Livro('Artificial Rocks', 'Geek University', 150)

console.print()

console.print("    [blue]def __mul__(self, outro):\n        [black]if isinstance(outro, int):\n            "
              "[cyan]msg = ''\n            [magenta]separador = ' | '  [white]# Adicionando um separador\n            "
              "[blue]for n in range(outro):\n                "
              "[black]msg += f'{self}{separador}' [white]# o self é o próprio objeto\n"
              "            [cyan]return msg.rstrip(separador)  [white]# Removendo o último separador antes de "
              "retornar[cyan]\n        [magenta]return 'Não posso multiplicar\n")

console.print("# ----------------------------------------------------------------------------------------")

console.print()

console.print(f'Livro 1: {livro1}')
console.print(f'Livro 2: {livro2}')

console.print()

console.print("[cyan]console.print(f'{livro1 * 3}')")

console.print()

console.print(f'Multiplicando o título: [yellow]{livro1 * 3}')

console.print()

console.print(f'Multiplicando por string: [yellow]{livro1 * "Geek"}')

console.print()

# ---------------------------------------------------------------------------------------------------------------------

texto = 'Sem usar __repr__() >> mostra o endereço de memória'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold green][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("[blue]\nclass Livro:\n\n    def __init__(self, titulo, autor, paginas):\n"
              ""
              "[black]        self.titulo = titulo\n"
              ""
              "[cyan]        self.autor = autor\n"
              ""
              "[magenta]        self.paginas = paginas\n"
              "")


# livro1 = Livro('Python Rocks', 'Geek University', 400)
# livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)


console.print("[cyan]console.print(f'{livro3}')")
console.print("[cyan]console.print(f'{livro4}')")


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __len__(self):
        return self.paginas


console.print()

console.print("# ----------------------------------------------------------------------------------------")

console.print()

# livro3 = Livro('Python Rocks', 'Geek University', 400)
# livro4 = Livro('Inteligência Artificial com Python', 'Geek University', 350)


console.print(f'[white]{livro3}')
console.print(f'[white]{livro4}')

console.print()

console.print("# ----------------------------------------------------------------------------------------")

console.print()

console.print("[yellow]Com método dunder __len__()\n\n"
              ""
              "    [black]def __len__(self):\n        return self.paginas\n")

console.print(f'O Livro {livro1} tem {len(livro1)} páginas')
console.print()
console.print(f'O Livro {livro2} tem {len(livro2)} páginas')
console.print()
console.print(f'O Livro {livro3} tem {len(livro3)} páginas')
console.print()
console.print(f'O Livro {livro4} tem {len(livro4)} páginas')
console.print()

console.print("[yellow]Com método dunder __add__()\n\n"
              ""
              "    [black]def __add__(self, outro):\n"
              "        return f'{self} - {outro}'\n\n"
              ""
              "[cyan]console.print(livro1 + livro2)")

console.print()

console.print("# ----------------------------------------------------------------------------------------")

console.print()

console.print(livro1 + livro2)

console.print()

console.print("# ----------------------------------------------------------------------------------------")

console.print()

console.print("[yellow]Com método dunder __del__()\n\n"
              ""
              "    [black]def __del__(self):\n        print('Um objeto do tipo Livro foi deletado da memória!')\n\n"
              "        [white]# se usar biblioteca externa rich(console.print()), dará o erro: "
              "[red]ImportError: sys.meta_path is None, Python is likely shutting down.\n")
