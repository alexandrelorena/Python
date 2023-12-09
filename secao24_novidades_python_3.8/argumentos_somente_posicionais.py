#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
argumentos_somente_posicionais

"""
from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Argumentos somente posicionais'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------\n")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ argumentos_somente_posicionais ↓
# --------------------------------------------------------------------------------------------------------------------

valor = '67.3'
print(float(valor))

console.print("[yellow]----------------------------------------------------------------------")

texto = 'cumprimenta_v1'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------")
def cumprimenta_v1(nome):
    return f'Ola {nome}'

print(cumprimenta_v1('Geek University - cumprimento 1'))
print(cumprimenta_v1(nome='Geek'))

console.print("[yellow]----------------------------------------------------------------------")

texto = 'cumprimenta_v2'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------")

def cumprimenta_v2(nome, /): # argumentos_somente_posicionais
    return f'Ola {nome}'

print(cumprimenta_v2('Geek University - cumprimento 2'))
# print(cumprimenta_v2(nome='Geek'))  # TypeError: cumprimenta_v2() got some positional-only arguments passed as keyword
                                      # arguments: 'nome'
console.print("[yellow]----------------------------------------------------------------------")

texto = 'cumprimenta_v3'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------")

def cumprimenta_v3(nome, /, mensagem='ola'):
    return f'{mensagem} {nome}'

print(cumprimenta_v3('Ale - cumprimento 3'))
print(cumprimenta_v3('University', mensagem='tudo bem?'))
print(cumprimenta_v3('University', 'oi'))

console.print("[yellow]----------------------------------------------------------------------")

texto = 'cumprimenta_v4'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------")
def cumprimenta_v4(nome, mensagem='Olá', /):
    return f'{mensagem} {nome}'

print(cumprimenta_v4('Geek - cumprimento 4'))
print(cumprimenta_v4('University', 'tudo bem?'))
# print(cumprimenta_v4('University', mensagem='e aí!'))  # somente posicional

console.print("[yellow]----------------------------------------------------------------------")

texto = 'cumprimenta_v5'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------")

def cumprimenta_v5(*, nome):  # '*' representa que um parâmetro é obrigatório
    return f'{nome}'

print(cumprimenta_v5(nome='Geek - cumprimento 5'))
# print(cumprimenta_v5('University'))  #TypeError: cumprimenta_v5() takes 0 positional arguments but 1 was given

console.print("[yellow]----------------------------------------------------------------------")

texto = 'cumprimenta_v6'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)

def cumprimentar_v6(nome, /, mensagem1='Olá', *, mensagem2):  # tudo antes da / é posicional | tudo após o * é obrigatório
    return f'{mensagem1} {nome} {mensagem2}'

print(cumprimentar_v6('Geek - cumprimento 6', mensagem1='tudo bem?', mensagem2='e aí!'))
print(cumprimentar_v6('Geek', mensagem2='tnha um bom dia!'))
# print(cumprimentar_v6('Geek', 'oi', 'cadê voce?'))  # TypeError: cumprimentar_v6() takes from 1 to 2 positional
                                                      # arguments but 3 were given


console.print("[yellow]----------------------------------------------------------------------")


