#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POO - atributos

Atributos -> representam as características do objeto. Divididos em 3 grupos:

    - Atributos de Instância
        * declarados dentro do método construtor (método especial para construção do objeto)
    - Atributos de Classe
    - Atributos Dinâmicos

# OBS:  O primeiro parametro do objeto SEMPRE será 'self'.
        Por comvenção, todo atributo de uma classe é público.
        Name Mangling => __ (duplo underscore) no início do nome do atributo é usado para deixá-lo privado.

        Utilizamos a palavra reservada 'class' para criar uma classe. A palavra pass é utilizada quando temos
        um código que ainda não foi implementado.

"""

# import shutil
from rich.console import Console
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

# -------------------------------------------- ↓ Bloco título ↓ --------------------------------------------
console = Console()

console.print()
texto = 'POO - atributos'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)


# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

# Classes com Atributo de Instância Públicos
texto = 'Classes com Atributo de Instância Públicos'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("[green]class [blue]Lampada:\n    def __init__(self, voltagem, cor):\n        self.voltagem = voltagem\n"
              "        self.cor = cor\n        self.ligada = False\n")


class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


console.print("[cyan]class [magenta]ContaCorrente:\n    def __init__(self, numero, limite, saldo):\n"
              "        self.numero = numero\n        self.limite = limite\n        self.saldo = saldo\n")


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


console.print("[blue]class [yellow]Produto:\n    def __init__(self, nome, descricao, valor):\n"
              "        self.nome = nome\n        self.descricao = descricao\n        self.valor = valor\n")


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


console.print("[red]class [white]Usuario:\n    def __init__(self, nome, email, senha):\n"
              "        self.nome = nome\n        self.email = email\n        self.senha = senha\n")


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


#  Atributos Públicos e Atributos Privados
texto = 'Atributos Públicos e Atributos Privados'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("[red]class [white]Acesso:\n    def __init__(self, email, senha):\n"
              "        self.email = email\n        self.__senha = senha\n")


class Acesso:
    def __init__(self, email, senha):
        self._Acesso__senha = None
        self.email = email  # com 2 underscore no início do atributo, é privado. APENAS CONVENÇÃO
        self.__senha = senha  # com 2 underscore no início do atributo, é privado. APENAS CONVENÇÃO

    @property
    def acesso__senha(self):
        return self._Acesso__senha


user = Acesso('user@gmail.com', '123456')

console.print("[blue]console.print(user.email)\n")
console.print(user.email)
console.print()
# console.print(user.__senha)  # AttributeError

# console.console.print(dir(user))

console.print("[blue]console.print(user._Acesso__senha)\n")
console.print(user.acesso__senha)  # Name Mangling
