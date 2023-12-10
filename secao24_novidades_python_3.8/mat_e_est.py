#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Funções Matemáticas e Estatísticas

• math.prod. → retorna o produto de um container numérico
• math.isqrt → retorna a raiz quadrada de um número
• math.dist → retorna a distância euclidiana entre dois pontos 3D ou 2D
• math.hypot → retorna a hipotenusa (norma Euclidiana)

• statistics.fmean → retorna a média de números reais
• statistics.geometric_mean → retorna a média geométrica de números reais
• statistics.multimode → retorna o valor mais frequente em uma sequência


• math.pow → retorna o valor de x elevado a y
• math.factorial → retorna o fatorial de um número
• math.factorial2 → retorna o fatorial de um número

• statistics.median → retorna a mediana de um container numérico
• statistics.mode → retorna o modo de um container numérico

• statistics.variance => retorna a variancia de um container numérico
• statistics.stdev → retorna o desvio padrao de um container numérico


"""
from rich.console import Console
import math
# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Funções Matemáticas e Estatísticas'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ Funções Matemáticas e Estatísticas ↓
# --------------------------------------------------------------------------------------------------------------------

texto = 'math.prod. → retorna o produto de um container numérico'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)

nuns_v1 = [2, 3, 6, 8]
nuns_v2 = (2, 3, 6, 8)
nuns_v3 = {2, 3, 6, 8}

"""
 2 * 3 * 6 * 8 -> 288
 
"""

console.print(f'Produtos: {math.prod(nuns_v1)}')
console.print(f'Produtos: {math.prod(nuns_v2)}')
console.print(f'Produtos: {math.prod(nuns_v3)}')

console.print("[yellow]----------------------------------------------------------------------")

texto = 'math.isqrt → retorna a raiz quadrada de um número'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)

console.print(math.isqrt(9))  # número inteiro (não arredonda valor)

console.print(math.sqrt(9))  # número real

console.print(math.isqrt(17))

console.print(math.sqrt(17))


console.print("[yellow]----------------------------------------------------------------------")

texto = 'math.dist → retorna a distância euclidiana entre dois pontos 3D ou 2D'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)
# Pontos 3D
p3d1 = (12, 50, 40)  # aqui sempre passa um container, não importa se tupla ou lista...
p3d2 = (10, 20, 30)

# Pontos 2D
p2d1 = [12, 50]
p2d2 = [10, 20]

console.print(math.dist(p3d1, p3d2))
console.print(math.dist(p2d1, p2d2))

console.print("[yellow]----------------------------------------------------------------------")

texto = 'math.hypot → retorna a hipotenusa (norma Euclidiana)'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)

console.print(math.hypot(*p3d1))  # desempacotamento

console.print(math.hypot(*p2d1))  # desempacotamento

console.print("[yellow]----------------------------------------------------------------------")

texto = 'statistics.fmean → retorna a média de números reais'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)

import statistics

valores_reais = [1.45, 3.45, 5.45, 7.45, 9.45]
valores_inteiros = [1, 6, 3, 89, 45]

console.print(statistics.fmean(valores_reais))
console.print(statistics.fmean(valores_inteiros))

console.print("[yellow]----------------------------------------------------------------------")

texto = 'statistics.geometric_mean → retorna a média geométrica de números reais'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)

console.print(statistics.geometric_mean(valores_reais))
console.print(statistics.geometric_mean(valores_inteiros))

console.print("[yellow]----------------------------------------------------------------------")

texto = 'statistics.multimode → retorna o valor mais frequente em uma sequência'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)

seq1 = 'Geek University'
seq2 = [3, 5, 3, 8, 7, 9, 5, 3]
seq3 = [1, 2, 3, 1, 2, 3, 4, 5, 6]

console.print(statistics.multimode(seq1))
console.print(statistics.multimode(seq2))
console.print(statistics.multimode(seq3))

console.print("[yellow]----------------------------------------------------------------------\n")
