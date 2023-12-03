#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
robo

"""
from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'robo'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ robo ↓
# --------------------------------------------------------------------------------------------------------------------

class Robo:

    def __init__(self, nome, bateria=100, habilidades=[]):
        self.__nome = nome
        self.__bateria = bateria
        self.__habilidades = habilidades

    @property
    def nome(self):
        return self.__nome

    @property
    def bateria(self):
        return self.__bateria

    @property
    def habilidades(self):
        return self.__habilidades

    def carregar(self):
        self.__bateria = 100

    def dizer_nome(self):
        if self.__bateria > 0:
            self.__bateria -= 1
            return f'BEEP BEEP BOOP. EU SOU O {self.__nome.upper()}'
        else:
            return 'Bateria fraca. Por favor, recarregue e tente novamente.'

    def aprender_habilidade(self, nova_habilidade, custo):
        if self.__bateria >= custo:
            self.__bateria -= custo
            self.__habilidades.append(nova_habilidade)
            return f'Uau! EU APRENDI {nova_habilidade.upper()}'
        return 'Bateria insuficiente. Por favor, recarregue e tente novamente.'

console.print("[yellow]#---------------------------------------------------------------------\n")
