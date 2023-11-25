#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
JSON e Pickle

JSON -> JavaScript Object Notation

Pickle -> Python object Notation

API -> Application Programming Interface

"""

from rich.console import Console
import json
import jsonpickle
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
# from csv import reader, DictReader

# -------------------------------------------- ↓ Bloco título ↓ --------------------------------------------

console = Console()

console.print()
texto = 'JSON e Pickle'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on blue][bold white][center]' + texto_centralizado)

# ---------------------------------------------------------------------------------------------------------------------
# ↓ Json ↓
# ---------------------------------------------------------------------------------------------------------------------

console.print("[cyan]\nret = json.dumps(['produto', {'PlayStation 4': ('2TB', 'Novo', '220V', 2340)}])\n")

ret = json.dumps(['produto', {'PlayStation 4': ('2TB', 'Novo', '220V', 2340)}])
# dumps formata as aspas as deixando duplas

# console.print("[yellow]\n# comando: ", end='')
# console.print("[black]console.print(f'tipo: {type(ret)} \ n conteúdo: {ret}')")

# console.print("[yellow]\n# saída esperada:\n", end='')
console.print(f'tipo: {type(ret)}\nconteúdo: {ret}')

# console.print("tipo: <class 'str'>")
# console.print('conteúdo: ["produto", {"PlayStation 4": ["2TB", "Novo", "220V", 2340]}]')

console.print()

console.print("[yellow]#---------------------------------------------------------------------\n")
class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'Vira-lata')

print(felix.__dict__)

ret = json.dumps(felix.__dict__)

print(ret)

console.print("[yellow]\n#---------------------------------------------------------------------\n")

# ---------------------------------------------------------------------------------------------------------------------
# ↓ Integrando o Json com o Pickle ↓
# ---------------------------------------------------------------------------------------------------------------------

ret = jsonpickle.encode(felix)

print(ret)

# ---------------------------------------------------------------------------------------------------------------------
# ↓ Escrevendo o arquivo jason/pickle ↓
# ---------------------------------------------------------------------------------------------------------------------

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)  # função encode -> modela o objeto para o formato jsonpickle.
    arquivo.write(ret)

console.print("[yellow]\n#---------------------------------------------------------------------\n")

# ---------------------------------------------------------------------------------------------------------------------
# ↓ Lendo o arquivo jason/pickle ↓
# ---------------------------------------------------------------------------------------------------------------------

with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)  # função decode -> transforma o arquivo json em um objeto python.
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
