#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
metadata

"""
from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Metadata'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ Metadata ↓
# --------------------------------------------------------------------------------------------------------------------
from importlib import metadata

console.print(f"[cyan]{metadata.version('pip')}")

console.print("[yellow]----------------------------------------------------------------------\n")

metadados_pip = metadata.metadata('pip')

console.print(list(metadados_pip))

console.print("[yellow]----------------------------------------------------------------------\n")

console.print(metadados_pip['Project-URL'])

console.print("[yellow]----------------------------------------------------------------------\n")

console.print(len(metadata.files('pip')))

console.print(metadata.requires('pip'))

console.print("[yellow]----------------------------------------------------------------------\n")

console.print(metadata.requires('django'))
