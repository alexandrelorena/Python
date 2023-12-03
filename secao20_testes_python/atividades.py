#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
atividades

"""
from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'atividades'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ atividades ↓
# --------------------------------------------------------------------------------------------------------------------


def comer(comida, eh_saudavel):
    pass

def dormir(num_horas):
    pass





console.print("[yellow]#---------------------------------------------------------------------\n")
