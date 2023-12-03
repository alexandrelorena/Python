#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
testes

"""
import unittest

from atividades import comer, dormir, eh_engracada
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
    def test_comer_saudavel(self):
        """Testando o retorno com comida saudável."""
        self.assertEqual(
            comer("quiabo", True),
            "Estou comendo quiabo porque quero manter a forma!"
        )

    def test_comer_gostosa(self):
        """Testando o retorno com comida gostosa."""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            "Estou comendo pizza porque a gente só vive uma vez!"
        )

    def test_dormir_pouco(self):
        """Testando o retorno dormir pouco."""
        self.assertEqual(
            dormir(4),
            "Continuo cansado após dormir por 4 horas. :("
        )

    def test_dormir_muito(self):
        """Testando o retorno dormir muito."""
        self.assertEqual(
            dormir(10),
            "Ufa! Dormi muito! Estou atrasado para o trabalho!"
        )

    def test_eh_engracada(self):
        """Testando o retorno se pessoa é graciosa."""
        # self.assertEqual(eh_engracada("Sérgio Malandro"), False)
        self.assertFalse(eh_engracada('Sérgio Malandro'))
        self.assertTrue(eh_engracada('Jim Carrey'), 'Jim Carrey deveria ser engraçado')

if __name__ == "__main__":
    unittest.main()  # Roda todos os testes


console.print("[yellow]#---------------------------------------------------------------------\n")
