#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Game: Calculadora — Curso Programação em Python do básico ao avançado
@Author: Geek University

"""
# from rich.console import Console
from models.calcular import Calcular

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------
#
# console = Console()
#
# console.print()
# texto = 'Game'
# tamanho_desejado = 70  # Largura do bloco
# texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
#
# console.print(f'[on magenta][bold white][center]' + texto_centralizado)
#
# console.print("[yellow]----------------------------------------------------------------------\n")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ teste ↓
# --------------------------------------------------------------------------------------------------------------------

calc: Calcular = Calcular(1)

print(calc)
