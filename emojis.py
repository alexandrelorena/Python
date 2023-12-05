#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Emojis

"""
# from rich.console import Console
from tabulate import tabulate
# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

# console = Console()
#
# console.print()
# texto = 'Emojis'
# tamanho_desejado = 70  # Largura do bloco
# texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
#
# console.print(f'[on magenta][bold white][center]' + texto_centralizado)
#
# console.print("[yellow]----------------------------------------------------------------------\n")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ emojis ↓
# --------------------------------------------------------------------------------------------------------------------

#  NÃO FUNCIONA DIREITO com CONSOLE.PRINT ou com EMULATE TERMINAL OUTPUT CONSOLE

print()

# console.print("[yellow]----------------------------------------------------------------------\n")

data = [
    ['Alt + 1', '☺'],
    ['Alt + 2', '☻'],
    ['Alt + 3', '♥'],
    ['Alt + 4', '♦'],
    ['Alt + 5', '♣'],
    ['Alt + 6', '♠'],
    ['Alt + 7', '•'],
    ['Alt + 8', '◘'],
    ['Alt + 9', '○'],
    ['Alt + 10', '◙'],
    ['Alt + 11', '♂'],
    ['Alt + 12', '♀'],
    ['Alt + 13', '♪'],
    ['Alt + 14', '♫'],
    ['Alt + 15', '☼'],
    ['Alt + 16', '►'],
    ['Alt + 17', '◄'],
    ['Alt + 18', '↕'],
    ['Alt + 20', '¶'],
    ['Alt + 21', '§'],
    ['Alt + 22', '▬'],
    ['Alt + 23', '↨'],
    ['Alt + 24', '↑'],
    ['Alt + 25', '↓'],
    ['Alt + 26', '→'],
    ['Alt + 27', '←'],
    ['Alt + 28', '∟'],
    ['Alt + 29', '↔'],
    ['Alt + 30', '▲'],
    ['Alt + 31', '▼'],
    ['Alt + 127', '⌂'],
    ['Alt + 145', 'æ'],
    ['Alt + 146', 'Æ'],
    ['Alt + 155', 'ø'],
    ['Alt + 156', '£'],
    ['Alt + 157', 'Ø'],
    ['Alt + 158', '×'],
    ['Alt + 159', 'ƒ'],
    ['Alt + 168', '¿'],
    ['Alt + 169', '®'],
    ['Alt + 174', '«'],
    ['Alt + 175', '»'],
    ['Alt + 176', '░'],
    ['Alt + 177', '▒'],
    ['Alt + 178', '▓'],
    ['Alt + 180', '┤'],
    ['Alt + 184', '©'],
    ['Alt + 185', '╣'],
    ['Alt + 186', '║'],
    ['Alt + 187', '╗'],
    ['Alt + 188', '╝'],
    ['Alt + 189', '¢'],
    ['Alt + 190', '¥'],
    ['Alt + 191', '┐'],
    ['Alt + 192', '└'],
    ['Alt + 193', '┴'],
    ['Alt + 194', '┬'],
    ['Alt + 195', '├'],
    ['Alt + 197', '┼'],
    ['Alt + 200', '╚'],
    ['Alt + 201', '╔'],
    ['Alt + 202', '╩'],
    ['Alt + 203', '╦'],
    ['Alt + 204', '╠'],
    ['Alt + 205', '═'],
    ['Alt + 206', '╬'],
    ['Alt + 207', '¤'],
    ['Alt + 208', 'ð'],
    ['Alt + 209', 'Ð'],
    ['Alt + 217', '┘'],
    ['Alt + 218', '┌'],
    ['Alt + 219', '█'],
    ['Alt + 220', '▄'],
    ['Alt + 221', '¦'],
    ['Alt + 223', '▀'],
    ['Alt + 225', 'ß'],
    ['Alt + 230', 'µ'],
    ['Alt + 231', 'þ'],
    ['Alt + 232', 'Þ'],
    ['Alt + 241', '±'],
    ['Alt + 242', '‗'],
    ['Alt + 245', '§'],
    ['Alt + 247', '¸'],
    ['Alt + 254', '■']
]

# Dividir os dados em quatro colunas
data = [data[i:i+4] for i in range(0, len(data), 4)]

print(tabulate(data, tablefmt="youtrack"))
