#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Checagem de Tipos com MyPy

"""
from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Checagem de Tipos com MyPy'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------\n")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ Checagem de Tipos com MyPy ↓
# --------------------------------------------------------------------------------------------------------------------

#  Só faz sentido usar o MyPy se utilizar a abordagem Type Hinting (trabalham em conjunto) => (Python avançado)

def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
         return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(70, '♫')

console.print(cabecalho("geek university"))

console.print(cabecalho("com type hinting", alinhamento=False))

console.print(cabecalho("com type hinting", alinhamento=True))

console.print()

cabecalho(texto='4', alinhamento=True)


console.print("[yellow]----------------------------------------------------------------------\n")
