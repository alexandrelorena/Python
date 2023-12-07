#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tipos em Python, na Prática

"""
from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Tipos em Python, na Prática'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------\n")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ jogo_cartas_v1 ↓
# --------------------------------------------------------------------------------------------------------------------

console.print("[yellow]----------------------------------------------------------------------\n")
