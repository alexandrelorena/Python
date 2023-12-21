#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__init__.py

"""
from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = '__init__.py'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------\n")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ __init__.py ↓
# --------------------------------------------------------------------------------------------------------------------

console.print("[yellow]----------------------------------------------------------------------\n")
