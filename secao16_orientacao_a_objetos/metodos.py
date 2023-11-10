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

* Métodos de Classe usam Decorators

* Métodos de classe são conhecidos como 'métodos estáticos' em outras linguagens.

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
texto = 'POO - Métodos'
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
              "   self.__ligada = False\n")


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

    def __init__(self, nomeprod, descricao, valorprod):
        self.__id = Produto.contador
        self.__nomeprod = nomeprod
        self.__descricao = descricao
        self.__valorprod = valorprod
        Produto.contador += 1

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valorprod * (100 - porcentagem)) / 100

    def valor_com_desconto(self, porcentagem):
        """Retorna o valor do desconto em Reais"""
        return self.__valorprod - self.desconto(porcentagem)


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

    def __init__(self, nomeuser, sobrenomeuser, emailuser, senhauser):
        self.__nomeuser = nomeuser
        self.__sobrenomeuser = sobrenomeuser
        self.__emailuser = emailuser
        self.__senhauser = cryp.hash(senhauser, rounds=2000000, salt_size=16)

    def nome_completo(self):
        return f'{self.__nomeuser} {self.__sobrenomeuser}'

    def checa_senha(self, senhauser):
        if cryp.verify(senhauser, self.__senhauser):
            return True
        return False


user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')

user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '654321')

# ---------------------------------------------------------------------------------------------------------------------

print(user1.nome_completo())  # o 'self' é o user1

print(Usuario.nome_completo(user1))  # o passando a classe 'Usuario e a instância 'nome_completo'.

print(user2.nome_completo())  # o 'self' é o user2

# print(f'Senha User 1: {user1._Usuario__senha}')  # Acesso de forma ERRADA de um atributo de classe.
#
# print(f'Senha User 2: {user2._Usuario__senha}')  # Acesso de forma ERRADA de um atributo de classe.
#

"""nome = input('\n\nInforme o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

user = None

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere!!!')
    exit(1)

print('Usuário criado com sucesso"')

senha_acesso = input('Informe a senha para acesso: ')


if user.checa_senha(senha_acesso):
    print('Acesso permitido')

else:
    print('Acesso negado!!!')
"""

texto = 'Métodos de Classe'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

# print(f'Senha User Criptografada: {user._Usuario__senha}')

console.print()

console.print("[red]class [white]Usuario:\n\n    contador = 0\n\n    [green]@classmethod  [white]# Decorators são "
              "necessários para criar métodos de Classe\n    [green]def conta_usuarios(cls):  [white]# método de "
              "classe\n        [green]print(f'Classe: {cls}')\n        print(f'Temos {cls.contador} usuário(s) no "
              "sistema!')\n\n"
              "    [black]@classmethod\n    def ver(cls):\n        print('Teste')\n\n"
              "    @staticmethod  [white]# método estático\n    [black]def definicao():\n        return 'UXR344'\n\n"

              "[blue]    def __init__(self, nomeuser, sobrenomeuser, emailuser, senhauser):\n        "
              "self.__id = Usuario.contador + 1\n        self.__nomeuser"
              " = nomeuser\n        self.__emailuser = emailuser\n        self.__senhauser = cryp.hash(senhauser, "
              "rounds=2000000, salt_size=16)\n        Usuario.contador = self.__id\n        print(f'Usuário criado: "
              "{self.__gera_usuario()}')\n\n    "
                          
              "[yellow]def nome_completo(self):\n        return f'{self.__nomeuser} {self.__sobrenomeuser}'\n\n"
              
              "    [magenta]def checa_senha(self, senhauser):  [white]# método de instância\n"
              "        [magenta]if cryp.verify(senhauser, self.__senhauser):\n            return True\n"
              "        return False\n\n"
                      
              "[cyan]    def __gera_usuario(self):  [white]# método privado - só é possível acessá-lo dentro da classe"
              "\n        [cyan]return self.__emailuser.split('@')[0]  [white]# split "
              "dividindo a string e retornando o slice 0\n\n")

console.print("user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')\n")

console.print("user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '654321')\n")

console.print("Usuario.conta_usuarios()  [blue]# Forma correta (nome da classe)\n")

console.print("user1.conta_usuarios()  [red]# Possível, mas incorreta (instância da classe)\n")


class Usuario:

    contador = 0

    @classmethod  # Decorators são necessários para criar métodos de Classe
    def conta_usuarios(cls):  # método de classe
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema!')

    @classmethod
    def ver(cls):
        print('Teste')

    @staticmethod  # método estático
    def definicao():
        return 'UXR344'

    def __init__(self, nomeuser, sobrenomeuser, emailuser, senhauser):
        self.__id = Usuario.contador + 1
        self.__nomeuser = nomeuser
        self.__sobrenomeuser = sobrenomeuser
        self.__emailuser = emailuser
        self.__senhauser = cryp.hash(senhauser, rounds=2000000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    #  Métodos de instância são criados pela necessidade de ter acesso a atributos de instãncia;
    def nome_completo(self):  # método de instância
        return f'{self.__nomeuser} {self.__sobrenomeuser}'

    def checa_senha(self, senhauser):  # método de instância
        if cryp.verify(senhauser, self.__senhauser):
            return True
        return False

    def __gera_usuario(self):  # método privado - só é possível acessá-lo dentro da classe
        return self.__emailuser.split('@')[0]  # split dividindo a string e retornando o slice 0


user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')

user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '654321')

Usuario.conta_usuarios()  # Forma correta (nome da classe)

user1.conta_usuarios()  # Possível, mas incorreta (instância da classe)

texto = 'Métodos Estáticos'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

#  Método de instância temos acesso a instância do objeto

#  Método de classe, não temos acesso a instância do objeto

# Método estático, não temos acesso a classe e nem a instância


print(Usuario.contador)

print(Usuario.definicao())

user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')

print(user1.contador)

print(user1.definicao())
