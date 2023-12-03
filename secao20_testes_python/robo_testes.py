#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
robo_testes

"""
from rich.console import Console
import unittest
from robo import Robo

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'robo_testes'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ robo_testes - setup() tearDown() ↓
# --------------------------------------------------------------------------------------------------------------------

texto = '↓ Utilizando setup() e tearDown() ↓'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 70)
console.print(f'[bold yellow][center]' + texto_centralizado)
console.print(f'[yellow]-' * 70)
class RoboTestes(unittest.TestCase):

    def setUp(self):
        self.megaman = Robo('Mega Man', bateria=50)
        print('setUp() sendo executado...')
    def test_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(self.megaman.dizer_nome(), 'BEEP BEEP BOOP. EU SOU O MEGA MAN')
        self.assertEqual(self.megaman.bateria, 49, 'A bateria deveria estar em 49%')

    def tearDown(self):
        print('Tear down() sendo executado...')


if __name__ == '__main__':
    unittest.main()

console.print("[yellow]#---------------------------------------------------------------------\n")
