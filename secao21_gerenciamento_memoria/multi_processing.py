#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
multi_processing

"""
from multiprocessing import Pool
import time
from rich.console import Console
# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Multi processing'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ Multi processing ↓
# --------------------------------------------------------------------------------------------------------------------


CONTADOR = 50000000

def contagem_regressiva(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':

    # inicio = time.time()
    #
    # pool = Pool(processes=2)
    # pool.map(contagem_regressiva, [CONTADOR // 2, CONTADOR // 2])
    # pool.close()
    # pool.join()
    #
    # fim = time.time()

    pool = Pool(processes=2)
    inicio = time.time()
    r1 = pool.apply_async(contagem_regressiva, [CONTADOR//2])
    r2 = pool.apply_async(contagem_regressiva, [CONTADOR//2])
    pool.close()
    pool.join()
    fim = time.time()


    console.print(f'[blue]Tempo de execução: {fim - inicio} segundos')


console.print("[yellow]----------------------------------------------------------------------\n")
