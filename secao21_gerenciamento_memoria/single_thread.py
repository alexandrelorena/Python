#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
single_thread

"""
from rich.console import Console
import time
# from threading import Thread

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = ' GIL - Python Global Interpreter Lock'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ single_thread ↓
# --------------------------------------------------------------------------------------------------------------------

texto = '↓ Single thread ↓'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 70)
console.print(f'[bold yellow][center]' + texto_centralizado)
console.print(f'[yellow]-' * 70)

CONTADOR = 50000000


def contagem_regressiva(n):
    while n > 0:
        n -= 1

inicio = time.time()
contagem_regressiva(CONTADOR)
fim = time.time()

print(f'Tempo de execução: {fim - inicio}')

console.print("[yellow]----------------------------------------------------------------------\n")