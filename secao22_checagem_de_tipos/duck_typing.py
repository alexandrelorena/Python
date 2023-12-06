#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Duck Typing

— Está relacionado a tipagem dinância de dados;
— O tipo ou a classe do objeto é menos importante que os métodos que o definem.
"""
from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Duck Typing'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------\n")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ Duck Typing ↓
# --------------------------------------------------------------------------------------------------------------------

class CisneNegro:

    def __len__(self):
        return 42

livro = CisneNegro()

print(len(livro))

nome = 'Geek University'
lista = [12, 34, 55, 49]
dicio = {"carlos": 12, "vanessa": 34, "joana": 49}

#  Os três acima são similares. São 'containers de dados'. Uma ‘string’ nada mais é do que um vetor.
#  Se um determinado objeto parce com um pato, anda como um pato, nada como um pato, então é um pato (Duck Typing).
print(len(nome))
print(len(lista))
print(len(dicio))

# idade = 42
# peso = 81.4
#
# print(len(idade))  # TypeError: object of type 'int' has no len()

console.print("[yellow]----------------------------------------------------------------------\n")

def addition(a, b):
    return a + b

print(addition(2, 4))

# c = addition(a, b)
# print(c)

console.print("[yellow]----------------------------------------------------------------------\n")
