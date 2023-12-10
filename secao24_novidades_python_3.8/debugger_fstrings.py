#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
debugger_fstrings

"""
from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Debugger com fstrings'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------\n")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ Debugger com fstrings ↓
# --------------------------------------------------------------------------------------------------------------------

def multiplicar(num1: float, num2: float) -> float:
    return num1 * num2

resultado: float = multiplicar(4.2345, 6.7890)

console.print(f'O resultado é {resultado}')

console.print(f'O resultado é {multiplicar(9, 4):.2f}')

console.print(f'{(media := 8/2)} é a metade de {(media * 2)}')

# --------------------------------------------------------------------------------------------------------------------

geek: str = 'Geek University'

console.print(f"geek='{geek}'")

console.print(f'{geek=}')  # usando fstrings

console.print(f'{geek.upper()[::-1] = }') # Debug do fstring

console.print(f"geek.upper()[::-1] = 'YTISREVINU KEEG'")  # comparando




console.print("[yellow]----------------------------------------------------------------------\n")
