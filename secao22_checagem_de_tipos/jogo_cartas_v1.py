#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tipos em Python, na Prática - Jogo cartas v1

"""
from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Tipos em Python, na Prática - Jogo cartas v1'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------\n")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ jogo_cartas_v1 ↓
# --------------------------------------------------------------------------------------------------------------------

nomes: list = ['Geek', 'University']
console.print(f'[blue]Lista: {nomes}')

versoes: tuple = (3, 4, 7)
console.print(f'[cyan]Tupla: {versoes}')

opcoes: dict = {'ar': True, 'banco_couro': True}
console.print(f'[magenta]Dicionário: {opcoes}')

valores: set = {1, 2, 3, 4, 5, 6}
console.print(f'[green]Set: {valores}')

console.print(f'[white]Annotations: {__annotations__}')

# --------------------------------------------------------------------------------------------------------------------
console.print("[yellow]\n----------------------------------------------------------------------\n")

from typing import Dict, List, Tuple, Set

nomes: List[str] = ['Geek', 'University']
console.print(f'[blue]Lista: {nomes}')

versoes: Tuple[int, int, int] = (3, 4, 7)
console.print(f'[cyan]Tupla: {versoes}')

opcoes: Dict[str, bool] = {'ar': True, 'banco_couro': True}
console.print(f'[magenta]Dicionário: {opcoes}')

valores: Set[int] = {1, 2, 3, 4, 5, 6}
console.print(f'[green]Set: {valores}')

console.print(f'[white]Annotations: {__annotations__}')

console.print("[yellow]\n----------------------------------------------------------------------\n")

import random

NAIPES = '♠ ♡ ♢ ♣'.split()
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

def criar_baralho(aleatorio=False):
    """Cria um baralho com 52 cartas."""
    baralho = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho

# print(NAIPES)
# print(CARTAS)

# print(criar_baralho())  # Lista de tuplas (tuplas de string)

def distribuir_cartas(baralho):
    """Distribui 4 cartas para cada jogador."""
    return baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4]

# baralho = criar_baralho()
#
# print(distribuir_cartas(baralho))

def jogar():
    """Inicia um jogo de cartas para 4 jogadores."""
    cartas = criar_baralho(True)
    jogadores = 'P1 P2 P3 P4'.split()
    maos = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f'{jogador}: {carta}')

if __name__ == '__main__':
    jogar()
