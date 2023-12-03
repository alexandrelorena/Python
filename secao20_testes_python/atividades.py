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
    if eh_saudavel:
        final = 'quero manter a forma!'
    else:
        final = 'a gente só vive uma vez!'
    return f'Estou comendo {comida} porque {final}'

def dormir(num_horas):
    if num_horas > 8:
        return f'Ufa! Dormi muito! Estou atrasado para o trabalho!'
    else:
        return f'Continuo cansado após dormir por {num_horas} horas. :('


def eh_engracada(pessoa):
    comediantes = ['Jim Carrey', 'Bozo', 'Patati Patatá']
    if pessoa in comediantes:
        return True
    return False

console.print("[yellow]#---------------------------------------------------------------------\n")
