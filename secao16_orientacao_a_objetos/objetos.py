#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POO - Objetos

    - São instâncias da classe (como variáveis do tipo definido na classe).

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
from passlib.hash import pbkdf2_sha256 as cryp

# -------------------------------------------- ↓ Bloco título ↓ --------------------------------------------
console = Console()

console.print()
texto = 'POO - Objetos'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)


# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

# Classes com Atributo de Instância Públicos
texto = 'Métodos de Instância'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("[green]class [blue]Lampada:\n\n    def __init__(self, cor, voltagem, luminosidade):\n        "
              "self.__cor = cor\n        self.__voltagem = voltagem\n        self.__luminosidade = luminosidade\n     "
              "   self.__ligada = False\n\n"
              ""
              "    [green]def checa_lampada(self):\n        return self.__ligada\n\n"
              ""
              "    [black]def ligar_desligar(self):\n        if self.__ligada:\n            self.__ligada = False\n"
              "        else:\n            self.__ligada = True\n")


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


console.print("[cyan]class Cliente:\n    def __init__(self, nome, cpf):\n        self.__nome = nome\n"
              "        self.__cpf = cpf\n\n"
              ""
              "    [blue]def diz(self):\n        print(f'O cliente {self.__nome} diz oi!')\n")


class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz oi!')

        cc._ContaCorrente__cliente.diz()

console.print("[cyan]class [magenta]ContaCorrente:\n\n    contador = 4999\n\n    def __init__(self, limite, saldo):\n"
              "        self.__numero = ContaCorrente.contador + 1\n        self.__limite = limite\n        "
              "self.__saldo = saldo\n        self.__cliente = cliente\n        ContaCorrente.contador = self.__numero"
              "\n"
              ""
              "    def mostra_cliente(self):\n        print(f'O cliente é {self.__cliente._Cliente__nome}')\n")


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')


console.print("[blue]class [yellow]Produto:\n\n    contador = 0\n\n    def __init__(self, nome, descricao, valor):\n"
              "        self.__id = Produto.contador\n        self.nome = nome\n        self.descricao = descricao\n"
              "        self.valor = valor\n        Produto.contador += 1\n\n"
              ""
              "    [green]def desconto(self, porcentagem):"
              "\n        return (self.__valor * (100 - porcentagem)) / 100\n"
              ""
              "    def valor_com_desconto(self, porcentagem):\n        return self.__valor - self.desconto(porcentagem)"
              "\n")


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador
        self.nome = nome
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

console.print("[red]class [white]Usuario:\n    def __init__(self, nome, sobrenome, email, senha):\n"
              "        self.nome = nome\n        self.__sobrenome = sobrenome\n        self.__email = email\n        "
              "self.senha = senha\n\n    [yellow]def nome_completo(self):\n        "
              "return f'{self.__nome} {self.__sobrenome}'\n")

console.print("user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')")

console.print("user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '654321')")

console.print()


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=2000000, salt_size=16)

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


console.print("[red]class [white]Usuario:\n    def __init__(self, nome, sobrenome, email, senha):\n"
              "        self.nome = nome\n        self.__sobrenome = sobrenome\n        self.__email = email\n"
              "        self.__senha = cryp.hash(senha, rounds=2000000, salt_size=16)\n\n"
              ""
              "    [yellow]def nome_completo(self):\n        "
              "return f'{self.__nome} {self.__sobrenome}'\n\n"
              ""
              "    def checa_senha(self, senha):\n        if cryp.verify(senha, self.__senha):\n            return True"
              "\n        return False\n")


#  Instâncias/Objetos
lamp1 = Lampada('branca', 110, 60)

console.print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

lamp1.ligar_desligar()

console.print()

console.print(f'[blue]A lâmpada foi ligada!')

console.print()

console.print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

console.print()

lamp1.ligar_desligar()

console.print(f'[red]A lâmpada foi desligada!')

console.print()

console.print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')

user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '654321')

cli1 = cliente = Cliente('Angelina Jolie', '123.456.789-99')

cc = ContaCorrente(5000, 20000, cli1)

cc.mostra_cliente()

cc._ContaCorrente__cliente.diz()