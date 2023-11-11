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

console.print("[red]class [blue]Acesso:\n    def __init__(self, email, senha):\n"
              "        self.email = email\n        self.__senha = senha\n\n    "
              ""
              "[green]def mostra_senha(self):\n              print(self.__senha)\n\n"
              ""
              "    [magenta]def mostra_email(self):\n    print(self.email)\n\n"
              ""
              "[cyan]@property\n    def senha(self):\n        self._senha = nova_senha\n    return self._senha\n\n"
              ""
              "[yellow]@senha.setter\n    def senha(self, nova_senha):\n        self._senha = nova_senha\n\n")


class Acesso:
    def __init__(self, email, senha):
        self._senha = None  # Inicialize com None se não houver senha definida inicialmente, e
        self.email = email  # utilize apenas um underscore para indicar que é um atributo protegido
        self.__senha = senha  # Utilize dois underscores para indicar que é um atributo privado

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        # Adicione validações ou lógica adicional, se necessário
        self._senha = nova_senha


console.print("user = Acesso('user@gmail.com', '123456')\n")

user = Acesso('user@gmail.com', '123456')

console.print("[blue]console.print(user.email)\n")
console.print(user.email)
console.print()
# console.print(user.__senha)  # AttributeError

# console.console.print(dir(user))

console.print("[blue]user.mostra_senha()\n")
# console.print(user.acesso__senha)  # Name Mangling
user.mostra_senha()
console.print()
console.print("[blue]user.mostra_email()\n")
user.mostra_email()

# ---------------------------------------------------------------------------------------------------------------------

#  Atributos de Instância
texto = 'Atributos de Instância'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

user1 = Acesso('user1@gmail.com', '654321')
user2 = Acesso('user2@hotmail.com', '246835')

user1.mostra_email()
user1.mostra_senha()
console.print()
user2.mostra_email()
user2.mostra_senha()

# ---------------------------------------------------------------------------------------------------------------------

#  Atributos de Classe -> declarados diretamente na classe (fora do construtor).
texto = 'Atributos de Classe'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

#  Refatorando a classe Produto:

console.print("[red]class Produto:\n    imposto = 1.05 \n    contador = 0\n\n"
              "    def __init__(self, nome, descricao, valor)\n        self.id = Produto.contador + 1\n"
              "        self.nome = nome\n        self.descricao = descricao\n        "
              "self.valor = (valor * Produto.imposto)\n        Produto.contador = self.id\n")

console.print("[blue]p1 = Produto('PlayStation 4', 'Video game', 2300)\n")
console.print("[blue]p2 = Produto('Xbox 5', 'Video game', 4500)\n")


# noinspection PyRedeclaration
class Produto:
    # Atributo de classe => vale pra qualquer instãncia da classe
    imposto = 1.05  # 0.05% de impost
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('PlayStation 4', 'Video game', 2300)
p2 = Produto('Xbox 5', 'Video game', 4500)

console.print("console.print{p1.imposto} [red]# acesso possível mas incorreto de um atributo de classe")
console.print("console.print{p1.valor} [red]# acesso possível mas incorreto de um atributo de classe")

console.print()

console.print("console.print(Produto.imposto) [blue]# Acesso correto de um atributo de classe \n")
console.print(f'[red]Imposto: {Produto.imposto}')  # Acesso correto de um atributo de classe

console.print()

console.print(f"{p1.id} - [cyan]Produto: [/cyan]{p1.nome} | [cyan]valor original: {p1.valor / Produto.imposto}[/cyan] |"
              f" [cyan]valor com imposto: {p1.valor}[/cyan]")
console.print(f"{p2.id} - [cyan]Produto: [/cyan]{p2.nome} | [cyan]valor original: {p2.valor / Produto.imposto}[/cyan] |"
              f" [cyan]valor com imposto: {p2.valor}[/cyan]")

# ---------------------------------------------------------------------------------------------------------------------

#  Atributos Dinâmicos -> atributo de instância que pode ser criado em tempo de execução.
#  Exclusivo da instância que o criou.
texto = 'Atributos Dinâmicos em tempo de execução'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("[blue]p3 = Produto('PlayStation 4', 'Video game', 2300)\n")
console.print("[blue]p4 = Produto('Arroz', 'Mercearia', 5.99)\n")

p3 = Produto('PlayStation 4', 'Video game', 2300)
p4 = Produto('Arroz', 'Mercearia', 5.99)

# Criando atributo dinâmico em tempo de execução
console.print("[blue]p4.peso = '5kg'\n")
p4.peso = '5kg'  # Note que na classe Produto não existe o atributo peso

console.print("[cyan]console.print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p4.peso}"
              "')\n")
console.print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p4.peso}')

# console.print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')
# AttributeError: 'Produto' object has no attribute 'peso'

# ---------------------------------------------------------------------------------------------------------------------

texto = 'Deletando atributos'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print(p3.__dict__)
console.print(p4.__dict__)
console.print()
console.print("[blue]del p4.peso\n")
console.print("[blue]del p4.valor\n")
console.print("[blue]del p4.descricao\n")
console.print("[blue]console.print(p3.__dict__)\n")
console.print("[blue]console.print(p4.__dict__)\n")

del p4.peso
del p4.valor
del p4.descricao
console.print(p3.__dict__)
console.print(p4.__dict__)
console.print()
console.print(Produto.__dict__)
