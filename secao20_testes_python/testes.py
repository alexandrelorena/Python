#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
testes

"""
import unittest

from atividades import comer, dormir
from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'testes'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ testes ↓
# --------------------------------------------------------------------------------------------------------------------

class AtividadesTestes(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()  # Roda todos os testes


console.print("[yellow]#---------------------------------------------------------------------\n")
