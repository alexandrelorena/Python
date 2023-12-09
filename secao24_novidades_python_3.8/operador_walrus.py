#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Novidades Python 3.8

Operador Walrus — permite fazer a atribuição e o retorno de valor em uma mesma expressão
    - variavel := expressão

"""
from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Novidades Python 3.8 - operador walrus'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------\n")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ operador_walrus ↓
# --------------------------------------------------------------------------------------------------------------------

console.print(f'[cyan]Atribuido valor à variável: [blue]nome = "Geek University"\n')
console.print(f'[cyan]Imprimindo o valor da variável: [blue]print(nome)\n')

nome = 'Geek University'  # atribuição na variável
console.print(f'[magenta]{nome}')  # imprimindo o valor da variável
print()

console.print("[yellow]----------------------------------------------------------------------\n")

#  com operador walrus:
console.print(f'[red]# com operador walrus - [cyan]Atribuindo e imprimindo o valor da variável na mesma expressão:')
console.print(f'[blue]nome := "Geek University"')

print()
console.print(nome := f'[magenta]Geek University')  # atribuindo e imprimindo o valor da variável na mesma expressão
print()

console.print("[yellow]----------------------------------------------------------------------\n")
#
# cesta = []
# fruta = input('Informe a fruta: ')
# while fruta != 'jaca':
#     cesta.append(fruta)
#     fruta = input('Informe a fruta: ')
#
# console.print(cesta)
#
# console.print("[yellow]----------------------------------------------------------------------\n")
#
# #  com operador walrus:
console.print(f'[red]# com operador walrus:')

cesta = []
while (fruta := input('Informe a fruta: ')) != 'jaca': cesta.append(fruta)

console.print(cesta)

console.print("[yellow]----------------------------------------------------------------------\n")



