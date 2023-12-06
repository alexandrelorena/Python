#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Fazendo uso de Annotations

"""
from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Fazendo uso de Annotations'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------\n")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ Fazendo uso de Annotations ↓
# --------------------------------------------------------------------------------------------------------------------

def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
         return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(70, '♫')

console.print(cabecalho("geek university"))

console.print(cabecalho("com type hinting", alinhamento=False))

console.print(cabecalho("com type hinting", alinhamento=True))

console.print()

cabecalho(texto='4', alinhamento=True)

# --------------------------------------------------------------------------------------------------------------------

"""#  Correto:

texto: str

# Inicial:

texto:str
texto : str

#  Retorno correto:

) -> str

#  Retorno incorreto:

)->str
) ->str

#  Inicializar um valor => correto
alinhamento: bool = True

#  Inicializar um valor => incorreto
alinhamento:bool=False
alinhamento:bool= False
alinhamento:bool =False
alinhamento: bool=False
...
"""

console.print("[yellow]----------------------------------------------------------------------\n")

import math

def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio

console.print(circunferencia.__annotations__)  # {'raio': <class 'float'>, 'return': <class 'float'>}
print()
console.print(f'[magenta]Circunferência:[/magenta] {circunferencia(10)}')

# --------------------------------------------------------------------------------------------------------------------

nome: str = 'Geek University'

peso: float = 67.9

ativo: bool = True

print()

console.print(f'[yellow]Nome:[/yellow] {nome} | [yellow]Peso:[/yellow] {peso} | [yellow]Ativo:[/yellow] {ativo}')  # (nome, peso, ativo)

print()

console.print(f'[cyan]Annotations de Geek University => [blue]{__annotations__}\n')

# --------------------------------------------------------------------------------------------------------------------

console.print("[yellow]----------------------------------------------------------------------\n")

class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:   # dicionário
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando'

    def get_nome(self):
        return self.__nome

    def get_idade(self) -> int:
        return self.__idade

    def get_peso(self) -> float:
        return self.__peso


p = Pessoa(nome='Geek University', idade=37, peso=68.5)

console.print(f'[cyan]{p.get_nome()} tem {p.get_idade()} anos, pesa {p.get_peso()} kg. [blue]{p.andar()}!\n')

console.print(f'[blue]Annnotations de[/blue] [cyan]__dict__[/cyan] => {p.__dict__}\n')

console.print(f'[blue]Annnotations de[/blue] [cyan]andar[/cyan] => {p.andar.__annotations__}\n')

console.print(f'[blue]Annnotations de[/blue] [cyan]__init__[/cyan] => {p.__init__.__annotations__}\n')

# print(p.__annotations__)  #AttributeError: 'Pessoa' object has no attribute '__annotations__'
