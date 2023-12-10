#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
optimizacoes

"""
from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Optimizaçõees'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------\n")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ optimizacoes ↓
# --------------------------------------------------------------------------------------------------------------------

import collections
from timeit import timeit

Pessoa = collections.namedtuple('Pessoa', 'nome email') # Forma rápida de criar classe
felicity = Pessoa('Felicity Jones', 'felicity@gmail.com')

console.print(felicity)

console.print(timeit('felicity.email', globals=globals()))  # calcula o tempo necessário para encontrar email

import sys

console.print(sys.getsizeof(list(range(31122023))))  # calcula quantidade de bytes necessários para gerar

console.print("[yellow]----------------------------------------------------------------------\n")
