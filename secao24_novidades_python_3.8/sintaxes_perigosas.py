#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Alertas sobre sintaxes perigosas

== ⇾ é usado para checar valor

is ⇾ é usado para checar se os objetos são os mesmos

"""
from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Alertas sobre sintaxes perigosas'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------\n")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ sintaxes_perigosas ↓
# --------------------------------------------------------------------------------------------------------------------

console.print("<stdin>:2: [red]SyntaxWarning:[/red] 'str' object is not callable; perhaps you missed a comma?")


console.print("[yellow]----------------------------------------------------------------------\n")
