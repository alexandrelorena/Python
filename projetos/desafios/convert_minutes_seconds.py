#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
convert_minutes_seconds

"""
from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'convert_minutes_seconds'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------\n")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ convert_minutes_seconds ↓
# --------------------------------------------------------------------------------------------------------------------

console.print(f'[blue]Write a function that takes an integer minutes and converts it to seconds.\n')
def convert(minutes: int) -> int:
    return minutes * 60

console.print(f'2 minutes = {convert(2)} seconds')

console.print(f'3 minutes = {convert(3)} seconds')

console.print(f'4 minutes = {convert(4)} seconds')

console.print(f'5 minutes = {convert(5)} seconds')


console.print("[yellow]----------------------------------------------------------------------\n")
