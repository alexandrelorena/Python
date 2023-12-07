#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tipos em comentarios

"""
from rich.console import Console

import math
# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Tipos em comentarios'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ Tipos em comentarios ↓
# --------------------------------------------------------------------------------------------------------------------

texto = '↓ Circunferência ↓'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[bold yellow][center]' + texto_centralizado)
console.print(f'[yellow]-' * 70)


def circunferencia(raio):
    # type: (float) -> float  # Type Hinting em comentarios
    return 2 * math.pi * raio

console.print(circunferencia(8))

# console.print(circunferencia('Geek'))

# --------------------------------------------------------------------------------------------------------------------

texto = '↓ Cabeçalho 1 ↓'
tamanho_desejado = 70  # Largura do bloco
console.print(f'[yellow]-' * 70)
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[bold yellow][center]' + texto_centralizado)
console.print(f'[yellow]-' * 70)


def cabecalho1(texto, alinhamento=False):
    # type: (str, bool) -> str
    if alinhamento:
        return f'[blue]Alinhamento ok"!'
    else:
        return f'[red]Alinhamento não ok!'

console.print(cabecalho1('Geek'))

# cabecalho1(texto=43, alinhamento='Geek')

# --------------------------------------------------------------------------------------------------------------------

texto = '↓ Cabeçalho 2 ↓'
tamanho_desejado = 70  # Largura do bloco
console.print(f'[yellow]-' * 70)
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[bold yellow][center]' + texto_centralizado)
console.print(f'[yellow]-' * 70)


def cabecalho2(
        texto,  # type: str
        alinhamento=True #type: bool
):  # type: (...) -> str
    if alinhamento:
        return f'[blue]Alinhamento ok"!'
    else:
        return f'[red]Alinhamento não ok!'

cabecalho2(texto='42', alinhamento=False)

nome = 'Geek University'  # type: str
console.print(f'[cyan]{cabecalho2(nome)}')

console.print(cabecalho2('Geek'))


console.print("[yellow]----------------------------------------------------------------------\n")
