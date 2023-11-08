#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POO - Métodos

Representam os comportamentos do objeto.

* A função do método especial dunder init __init__ , chamado de construtor, é
construir o objeto a partir da classe.

* Dunder -> Double Underline (duplo undernline): Todo elemento em Python que inicia e termina com o duplo underline.

* Os métodos/funções dunder em Python são chamados de métodos mágicos.

* Não é recomendado criar métodos com nomes com dunder. Ex: def __correr__(self, metros):

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
texto = 'POO - Métodos'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)


# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

# Classes com Atributo de Instância Públicos
texto = 'Métodos de Classe'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("[green]class [blue]Lampada:\n\n    def __init__(self, cor, voltagem, luminosidade):\n        "
              "self.__cor = cor\n        self.__voltagem = voltagem\n        self.__luminosidade = luminosidade\n     "
              "   self.__ligada = False\n\n")


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


console.print("[cyan]class [magenta]ContaCorrente:\n\n    contador = 4999\n\n    def __init__(self, limite, saldo):\n"
              "        self.__numero = ContaCorrente.contador + 1\n        self.__limite = limite\n        "
              "self.__saldo = saldo\n        ContaCorrente.contador = self.__numero\n")


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


console.print("[blue]class [yellow]Produto:\n\n    contador = 0\n\n    def __init__(self, nome, descricao, valor):\n"
              "        self.__id = None\n        self.nome = nome\n        self.descricao = descricao\n        "
              "self.valor = valor\n        Produto.contador = self.__id\n\n    [green]def desconto(self, porcentagem):"
              "\n        return (self.__valor * (100 - porcentagem)) / 100\n")


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador += 1

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100

    def valor_com_desconto(self, porcentagem):
        """Retorna o valor do desconto em Reais"""
        return self.__valor - self.desconto(porcentagem)


p1 = Produto('PlayStation 4', 'Video Game', 2300)

console.print(f'[blue]Produto com o desconto: R${p1.desconto(50):.2f}')

console.print(f'[magenta]Valor do desconto: R${p1.valor_com_desconto(50):.2f}')

console.print()

console.print("[red]class [white]Usuario:\n    def __init__(self, nome, email, senha):\n"
              "        self.nome = nome\n        self.email = email\n        self.senha = senha\n")


class Usuario:

    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    # def __correr__(self, metros):  # não recomendado criar métodos com nomes com dunder
    #     print(f'{self.__nome} está correndo {metros} metros')


console.print()

console.print("[cyan]class [magenta]ContaCorrente:\n    def __init__(self, numero, limite, saldo):\n"
              "        self.numero = numero\n        self.limite = limite\n        self.saldo = saldo\n")


# ---------------------------------------------------------------------------------------------------------------------
