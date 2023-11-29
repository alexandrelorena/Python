#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Doctests

"""


from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Assertions (Afirmações/Checagens/Questionamentos)'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ assert ↓
# --------------------------------------------------------------------------------------------------------------------

console.print("[yellow]#---------------------------------------------------------------------\n")

