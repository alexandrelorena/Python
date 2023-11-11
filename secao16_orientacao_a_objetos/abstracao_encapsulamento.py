#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POO - Abstraçãoo e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico
e hierárquico utilizando classes.

Exemplo - Acessando elementos privados fora da classe:

    classe: Pessoa
    atributo privado: __nome
    método privado: __falar()

_Classe__elemento

instancia._Pessoa__nome
instancia._Pessoa__falar()

*** NÃO DEVEMOS FAZER ESSE TIPO DE ACESSO apasar do python não bloquear!!!

- Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos
 e métodos privados de usuário.


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
texto = 'POO - Abstraçãoo e Encapsulamento'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)


# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

# Classes com Atributo de Instância Públicos
texto = 'Abstraçãoo e Encapsulamento'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("[blue]class Conta:\n\n    contador = 400\n\n    def __init__(self, titular, saldo, limite):\n"
              "        self.__numero = Conta.contador\n        self.__titular = titular\n        self.__saldo = saldo\n"
              "        self.__limite = limite\n        Conta.contador += 1\n\n"
              ""
              "    [cyan]def extrato(self):\n        print(f'Saldo de {self.__saldo} do titular {self.__titular} com "
              "limite de {self.__limite}')\n\n"
              ""
              "    [yellow]def depositar(self, valor):\n        if valor > 0:\n            self.__saldo += valor\n     "
              "       print(f'Depósito de {valor} realizado com sucesso.'\n            return valor\n        else:\n  "
              "          print('O valor precisa ser positivo!')\n\n"
              ""
              "    [black]def sacar(self, valor):\n        if valor > 0:\n            if self.__saldo >= valor:\n      "
              "          self.__saldo -= valor\n                print(f'Saque de {valor} realizado com sucesso.')\n    "
              "            return valor\n            else:\n                print('Saldo insuficiente para saque.')\n  "
              "              return 0  [white]# Retornando 0 para indicar que o saque não foi realizado\n        "
              "[black]else:\n            print('O valor deve ser positivo!')\n\n"
              ""
              "    [magenta]def transferir(self, valor, conta_destino):\n        [white]#  1 - Remover valor da conta "
              "de origem\n        [magenta]self.__saldo -= valor\n        self.__saldo -= 10  # taxa de transferência"
              "\n        [white]# 2 - Adicionar valor a conta de destino\n        "
              "[magenta]conta_destino.__saldo += valor\n\n")


class Conta:

    contador = 1
    # contador_formatado = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1
        self.__numero_formatado = f"{self.__numero:03d}"

    def extrato(self):
        console.print(f'[blue]Saldo de [green]{self.__saldo} [blue]do titular [yellow]{self.__titular} [blue]com limite'
                      f' de [cyan]{self.__limite}')

    def depositar(self, valor):
        if valor > 0:   # validação do depósito
            self.__saldo += valor
            console.print(f'[cyan]Depósito de [blue]{valor} [cyan]realizado com sucesso, [yellow]{self.__titular}')
            return valor
        else:
            print('O valor precisa ser positivo!')

    def sacar(self, valor):
        if valor > 0:   # varificando se saldo é positivo
            if self.__saldo >= valor:
                self.__saldo -= valor
                console.print(f'[yellow]{self.__titular}[magenta] - Saque de [red]{valor} [magenta]realizado com '
                              f'sucesso.')
                return valor
            else:
                console.print('[red]Saldo insuficiente para saque.')
                return 0  # Retornando  0 para indicar que o saque não foi realizado
        else:
            print('O valor deve ser positivo!')

    def transferir(self, valor, conta_destino):
        #  1 - Remover valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10  # taxa de transferência

        # 2 - Adicionar valor a conta de destino

        conta_destino.__saldo += valor


console.print("[blue]conta1 = Conta('Angelina', 150, 1500)\n")
console.print("[cyan]conta2 = Conta('Felicity', 300, 2000)\n")

conta1 = Conta('Angelina', 150, 1500)
conta2 = Conta('Felicity', 300, 2000)

contador_formatado = f"{Conta.contador:03d}"

console.print(f"[blue]Número da conta 1: [cyan]{conta1._Conta__numero_formatado}")
console.print(f"[blue]Número da conta 2: [cyan]{conta2._Conta__numero_formatado}")

console.print()

console.print("conta1.extrato()\n")
console.print("console.print(conta1.depositar(150))\n")
console.print("conta1.extrato()\n")

conta1.extrato()
conta1.depositar(150)
conta1.extrato()
conta1.sacar(100)
conta1.extrato()

console.print()
print(conta1.__dict__)
console.print()

console.print("conta2.extrato()\n")
console.print("console.print(conta2.depositar(150))\n")
console.print("conta2.extrato()\n")

conta2.extrato()
conta2.depositar(250)
conta2.extrato()
conta2.sacar(300)
conta2.extrato()

console.print()
print(conta2.__dict__)
console.print()

console.print(f'[cyan]Saldo da conta de {conta1._Conta__titular} antes do depósito:')
conta1.extrato()
console.print(f'[magenta]Saldo da conta de {conta2._Conta__titular} antes do depósito:')
conta2.extrato()

console.print()

conta2.transferir(100, conta1)
console.print(f'[cyan]Saldo da conta de {conta1._Conta__titular} depois do depósito:')
conta1.extrato()
console.print(f'[magenta]Saldo da conta de {conta2._Conta__titular} depois do depósito:')
conta2.extrato()
console.print()

# Name Mangling - acesso indevido fora da classe!
"""print(conta1._Conta__titular)
conta1._Conta__titular = 'Angelina'
print(conta1.__dict__)
"""