#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Doctests
— são testes que colocamos na docstring das funções/métodos Python.
Python -m doctest -v nome_do_modulo.py

# saída:

Trying:
    soma(1, 2)  # doctest (como no python console)
Expecting:
    3
ok
1 item had no tests:
    doctests
1 item passed all tests:
   1 tests in doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

"""

from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Doctests'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------


def soma(a, b):
    """soma os números a e b
    >>> soma(1, 2)  # doctest (no terminal: python -m doctest -v doctests.py
    3
    >>> soma(4, 6)
    10
    """
    return a + b

print(soma(3, 4))


console.print("[yellow]#---------------------------------------------------------------------\n")

# --------------------------------------------------------------------------------------------------------------------
# ↓ Outro exemplo - aplicando o TDD ↓
# --------------------------------------------------------------------------------------------------------------------


def duplicar(valores):
    """duplica os valores em uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]
    >>> duplicar([])
    []
    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar ([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]


def fala_oi():
    """Fala oi

    >>> fala_oi()
    'oi'
    """
    return "oi"

# Dentro do doctest, não reconhece aspas duplas (não passa no teste); necessário trocar por aspas simples.


def verdade():
    """Retorna verdade

    >>> verdade()
    True
    """
    return True

#  Cuidado com espaços e tab para não prejudicar o resultado do teste.
