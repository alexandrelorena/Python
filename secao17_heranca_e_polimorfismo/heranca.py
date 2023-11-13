#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POO - Heranca e Polimorfismo

* Reaproveitamento de código
* Extensão de classes

OBS: A partir de uma classe existente, extendemos outra classe que passa a
herdar atributos e métodos da classe herdada.

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

OBS: A classe que herda de outra classe, herda TODOS os atributos e métodos da classe
herdada.

#  A Classe herdada é conhecida como:
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;

# A Classe que herda de outra é conhecida por:
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;
#  Sobbrescrita de Método - ocorre quando reescrevemos/reiplementamos um método presente
na super classe em classes filhas.
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
texto = 'POO - Herança e Polimorfismo'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)


# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

texto = 'Sem Herança'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("[blue]class Cliente:\n    def __init__(self, nome, sobrenome, cpf, renda):\n        self.__nome = nome\n"
              "        self.__sobrenome = sobrenome\n        self.__cpf = cpf\n        self.__renda = renda\n\n"
              ""
              "    [cyan]def nome_completo(self):\n        return f'{self.__nome} {self.__sobrenome}'\n\n"
              ""
              "[green]class Funcionario:\n    def __init__(self, nome, sobrenome, cpf, matricula):\n        self.__nome"
              " = nome"
              "\n        self.__sobrenome = sobrenome\n        self.__cpf = cpf\n        self.__matricula = matricula"
              "\n\n    [black]def nome_completo(self):\n        return f'{self.__nome} {self.__sobrenome}'\n\n")


class Cliente:
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


console.print("cliente1 = Cliente('Angelina', 'Jolie', '123.456.789.00', 5000)")
console.print("funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321.99', 1234)")

console.print()

cliente1 = Cliente('Angelina', 'Jolie', '123.456.789.00', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321.99', 1234)

console.print("[white]console.print(cliente1.nome_completo()) [cyan]=>> ", end='')
console.print(f'[cyan]{cliente1.nome_completo()}')
console.print()

console.print("[white]console.print(funcionario1.nome_completo()) [cyan]=>> ", end='')
console.print(f'[cyan]{funcionario1.nome_completo()}')
console.print()

# ---------------------------------------------------------------------------------------------------------------------

texto = 'Com Herança'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("[blue]class Pessoa:\n    def __init__(self, nome, sobrenome, cpf):\n        self.__nome = nome\n"
              "        self.__sobrenome = sobrenome\n        self.__cpf = cpf\n\n"
              ""
              "    [cyan]def nome_completo(self):\n        return f'{self.__nome} {self.__sobrenome}'\n\n"
              ""
              "[magenta]class Cliente(Pessoa):  [white]# herança\n    [magenta]def __init__(self, nome, sobrenome, cpf,"
              " renda):\n        Pessoa.__init__(self, nome, sobrenome, cpf)  [white]# Forma não comum de acessar dados"
              " da super classe\n        [magenta]self.__renda = renda\n\n"
              ""
              "[black]class Funcionario:\n    def __init__(self, nome, sobrenome, cpf, matricula):\n        "
              "super().__init__(nome, sobrenome, cpf)  [white]# Forma comum de acessar dados da super classe\n"
              "        [black]self.__sobrenome = sobrenome\n        self.__cpf = cpf\n        self.__matricula = "
              "matricula\n\n")


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


class Cliente(Pessoa):  # herança
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma não comum de acessar dados da super classe
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma comum de acessar dados da super classe
        self.__matricula = matricula


console.print("cliente1 = Cliente('Angelina', 'Jolie', '123.456.789.00', 5000)")
console.print("funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321.99', 1234)")

console.print()

cliente1 = Cliente('Angelina', 'Jolie', '123.456.789.00', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321.99', 1234)

console.print("[white]console.print(cliente1.nome_completo()) [cyan]=>> ", end='')
console.print(f'[cyan]{cliente1.nome_completo()}')
console.print()

console.print("[white]console.print(funcionario1.nome_completo()) [cyan]=>> ", end='')
console.print(f'[cyan]{funcionario1.nome_completo()}')

console.print()

console.print(f'[yellow]{cliente1.nome_completo()}')
console.print("print(cliente1.__dict__)")
console.print(f'[blue]{cliente1.__dict__}')

console.print()

console.print(f'[yellow]{funcionario1.nome_completo()}')
console.print("print(funcionario1.__dict__)")
console.print(f'[blue]{funcionario1.__dict__}')

# ---------------------------------------------------------------------------------------------------------------------

texto = 'Sobrescrita de método'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("[blue]class Pessoa:\n    def __init__(self, nome, sobrenome, cpf):\n        self.__nome = nome\n"
              "        self.__sobrenome = sobrenome\n        self.__cpf = cpf\n\n"
              ""
              "    [cyan]def nome_completo(self):\n        return f'{self.__nome} {self.__sobrenome}'\n\n"
              ""
              "[magenta]class Cliente(Pessoa):  [white]# herança\n    [magenta]def __init__(self, nome, sobrenome, cpf,"
              " renda):\n        super().__init__(nome, sobrenome, cpf)  [white]# Forma não comum de acessar dados"
              " da super classe\n        [magenta]self.__renda = renda\n\n"
              ""
              "[black]class Funcionario:\n    def __init__(self, nome, sobrenome, cpf, matricula):\n        "
              "super().__init__(nome, sobrenome, cpf)  [white]# Forma comum de acessar dados da super classe\n"
              "        [black]self.__sobrenome = sobrenome\n        self.__cpf = cpf\n        self.__matricula = "
              "matricula\n\n    def nome_completo(self):\n        return f'[cyan]Funcionário: {self.__matricula} Nome: "
              "[blue]{super().nome_completo()} [cyan]CPF: {self.cpf}'\n\n")


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


class Cliente(Pessoa):  # herança
    """Cliente herda de Pessoa"""

    # def __init__(self, nome, sobrenome, cpf, renda):
    #     Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma não comum de acessar dados da super classe
    #     self.__renda = renda

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)  # Forma comum de acessar dados da super classe
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma comum de acessar dados da super classe
        self.__matricula = matricula

    def nome_completo(self):
        return f'[cyan]Funcionário: {self.__matricula} Nome: [blue]{super().nome_completo()} [cyan]CPF: {self.cpf}'


console.print("cliente1 = Cliente('Angelina', 'Jolie', '123.456.789.00', 5000)")
console.print("funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321.99', 1234)")

console.print()

cliente1 = Cliente('Angelina', 'Jolie', '123.456.789.00', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321.99', 1234)

console.print("[black]console.print(cliente1.nome_completo())")
console.print(cliente1.nome_completo())
console.print()
console.print("[black]console.print(funcionario1.nome_completo())")
console.print(funcionario1.nome_completo())
