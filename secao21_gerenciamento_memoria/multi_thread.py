#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
multi_thread

"""
from rich.console import Console
import time
from threading import Thread
# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'multi_thread'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ multi_thread ↓
# --------------------------------------------------------------------------------------------------------------------

texto = '↓ Utilizando 2 threads em paralelo ↓'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 70)
console.print(f'[bold yellow][center]' + texto_centralizado)
console.print(f'[yellow]-' * 70)

CONTADOR = 50000000

def contagem_regressiva(n):
    while n > 0:
        n -= 1

t1 = Thread(target=contagem_regressiva, args=(CONTADOR//2,))
t2 = Thread(target=contagem_regressiva, args=(CONTADOR//2,))

inicio = time.time()
t1.start()  # startando a primeira thread
t2.start() # startando a segunda thread
t1.join()  # executando a primeira thread
t2.join()  # executando a segunda thread
fim = time.time()

console.print(f'[blue]Tempo de execução: {fim - inicio}')

console.print("[yellow]----------------------------------------------------------------------\n")
