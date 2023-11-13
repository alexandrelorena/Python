#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POO - Propriedades (Properties)

* getters - retornam o valor do atributo

* setters - alteram o valor do atributo (menos seguro)

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
texto = 'POO - Propriedades (Properties)'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)


# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

texto = 'Usando getters and setters'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("[blue]class Conta:\n\n    contador = 0\n\n    def __init__(self, titular, saldo, limite):\n"
              "        self.__numero = Conta.contador + 1\n        self.__titular = titular\n        "
              "self.__saldo = saldo\n        self.__limite = limite\n        Conta.contador += 1\n\n"
              ""
              "    [cyan]    def extrato(self):\n        return f'Saldo de {self.__saldo} do cliente {self.__titular}'"
              "\n\n"
              ""
              "[black]    def depositar(self, valor):\n        self.__saldo += valor\n\n"
              ""
              "    [cyan]def sacar(self, valor):\n        self.__saldo -= valor\n\n"
              ""
              "    [blue]def transferir(self, valor, destino):\n        self.__saldo -= valor\n        destino.__saldo"
              " += valor\n\n"
              ""
              "    [cyan]def get_numero(self):\n        return self.__numero\n\n"
              ""
              "    [black]def get_titular(self):\n        return self.__titular\n\n"
              ""
              "    [cyan]def set_titular(self, titular):\n        self.__titular = titular\n\n"
              ""
              "    [blue]def get_saldo(self):\n        return self.__saldo\n\n"
              ""
              "    [cyan]def get_limite(self):\n        return self.__limite\n\n"
              ""
              "    [black]def set_limite(self, limite):\n        self.__limite = limite\n\n")


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente [yellow]{self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

console.print(conta1.extrato())
console.print(conta2.extrato())

soma = conta1.get_saldo() + conta2.get_saldo()  # Forma CORRETA de acessar atributos de fora da classe
console.print()
console.print(f'A soma das contas é {soma}')

# soma = conta1._Conta__saldo + conta2._Conta__saldo  # Forma NÃO RECOMENDADA acessar atributos de fora da classe
# console.print(f'A soma das contas é {soma}')

console.print()

console.print(f'[blue]{conta1.__dict__}')
conta1.set_limite(999999)
console.print(f'[magenta]{conta1.__dict__}')

# ---------------------------------------------------------------------------------------------------------------------

texto = 'Usando Properties'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("[blue]class Conta:\n\n    contador = 0\n\n    def __init__(self, titular, saldo, limite):\n"
              "        self.__numero = Conta.contador + 1\n        self.__titular = titular\n        "
              "self.__saldo = saldo\n        self.__limite = limite\n        Conta.contador += 1\n\n"
              ""
              "    [cyan]@property\n    def numero(self):\n        return self.__numero\n\n"
              ""
              "    [magenta]@property\n    def titular(self):\n        return self.__titular\n\n"
              ""
              "    [blue]@property\n    def saldo(self):\n        return self.__saldo\n\n"
              ""
              "    [black]@property\n    def limite(self):\n        return self.__limite\n\n"
              ""
              "    [cyan]@limite.setter  [white]# criando um setter para o property 'limite'\n    "
              "[cyan]def limite(self, novo_limite):\n        self.__limite = novo_limite\n\n"
              ""
              "    [magenta]def extrato(self):\n        return f'Saldo de {self.__saldo} do cliente [yellow]"
              "{self.__titular}'\n\n"
              ""
              "    [blue]def depositar(self, valor):\n        self.__saldo += valor\n\n"
              ""
              "    [black]def sacar(self, valor):\n        self.__saldo -= valor\n\n"
              ""
              "    [cyan]def transferir(self, valor, destino):\n        self.__saldo -= valor\n        "
              "destino.__saldo += valor\n\n"
              ""
              "    [magenta]@property\n    def valor_total(self):\n        return self.__saldo + self.__limite\n\n")


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter  # criando um setter para o property 'limite'
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente [yellow]{self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite


conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

console.print(conta1.extrato())
console.print(conta2.extrato())

soma = conta1.saldo + conta2.saldo  # Forma CORRETA de acessar atributos de fora da classe
console.print()
console.print(f'A soma das contas é {soma}')

console.print()

console.print(conta1.__dict__)

console.print()

conta1.limite = 7000

console.print(f'[blue]Alterando o limite da conta de [yellow]{conta1.titular} [blue]para: {conta1.limite}')

console.print()

console.print(conta1.__dict__)

console.print()

console.print(f'[blue]Total na conta de [yellow]{conta1.titular} [blue]=> saldo: {conta1.saldo} + limite: {conta1.limite} = {conta1.valor_total}')