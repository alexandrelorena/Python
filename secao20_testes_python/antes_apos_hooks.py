#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Unitests -Antes e após hooks

Hooks — são os testes em sim.

- setup() -> executado antes de cada método de teste. Útil para criar instâncias de objetos e outros dados.

- tearDown() -> executado ao final de cada método de teste. Útil para limpar dados e fechar conexões.

"""
from rich.console import Console
import unittest

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Antes e após hooks'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ antes_apos_hooks ↓
# --------------------------------------------------------------------------------------------------------------------

class ModuloTest(unittest.TestCase):

    def setup(self):
        # Configurações do setup()
        pass
    def test_primeiro(self):
        # setup vai rodar antes do teste
        # tearDown vai rodar depois do teste
        pass

    def test_segundo(self):
        # setup vai rodar antes do teste
        # tearDown vai rodar depois do teste
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass


console.print("[yellow]#---------------------------------------------------------------------\n")
