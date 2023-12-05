#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Type Hinting - pep 484

"""
from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Type Hinting'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------\n")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ Type Hinting ↓
# --------------------------------------------------------------------------------------------------------------------

# def cumprimentar(nome: str) -> str:
#     return f"Olá {nome}"
#
# console.print(cumprimentar("Joaquim"))


def cabecalho(texto, alinhamento=True):
    if alinhamento:
         return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(70, '=')

console.print(cabecalho("geek university"))

console.print(cabecalho("sem type hinting", alinhamento=False))


console.print("[yellow]----------------------------------------------------------------------\n")


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
         return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(70, '♫')

console.print(cabecalho("geek university"))

console.print(cabecalho("com type hinting", alinhamento=False))

console.print()

print(f" Alt + 1 ".center(70, '☺'))
print(f" Alt + 2 ".center(70, '☻'))
print(f" Alt + 3 ".center(70, '♥'))
print(f" Alt + 4 ".center(70, '♦'))
print(f" Alt + 5 ".center(70, '♣'))
print(f" Alt + 6 ".center(70, '♠'))
print(f" Alt + 7 ".center(70, '•'))
print(f" Alt + 8 ".center(70, '◘'))
print(f" Alt + 9 ".center(70, '○'))
print(f" Alt + 10 ".center(70, '◙'))
print(f" Alt + 11 ".center(70, '♂'))
print(f" Alt + 12 ".center(70, '♀'))
print(f" Alt + 13 ".center(70, '♪'))
print(f" Alt + 14 ".center(70, '♫'))
print(f" Alt + 15 ".center(70, '☼'))
print(f" Alt + 16 ".center(70, '►'))
print(f" Alt + 17 ".center(70, '◄'))
print(f" Alt + 18 ".center(70, '↕'))
print(f" Alt + 20 ".center(70, '¶'))
print(f" Alt + 21 ".center(70, '§'))
print(f" Alt + 22 ".center(70, '▬'))
print(f" Alt + 23 ".center(70, '↨'))
print(f" Alt + 24 ".center(70, '↑'))
print(f" Alt + 25 ".center(70, '↓'))
print(f" Alt + 26 ".center(70, '→'))
print(f" Alt + 27 ".center(70, '←'))
print(f" Alt + 28 ".center(70, '∟'))
print(f" Alt + 29 ".center(70, '↔'))
print(f" Alt + 30 ".center(70, '▲'))
print(f" Alt + 31 ".center(70, '▼'))
print(f" Alt + 127 ".center(70, '⌂'))
print(f" Alt + 145 ".center(70, 'æ'))
print(f" Alt + 146 ".center(70, 'Æ'))
print(f" Alt + 155 ".center(70, 'ø'))
print(f" Alt + 156 ".center(70, '£'))
print(f" Alt + 157 ".center(70, 'Ø'))
print(f" Alt + 158 ".center(70, '×'))
print(f" Alt + 159 ".center(70, 'ƒ'))
print(f" Alt + 168 ".center(70, '¿'))
print(f" Alt + 169 ".center(70, '®'))
print(f" Alt + 174 ".center(70, '«'))
print(f" Alt + 175 ".center(70, '»'))
print(f" Alt + 176 ".center(70, '░'))
print(f" Alt + 177 ".center(70, '▒'))
print(f" Alt + 178 ".center(70, '▓'))
print(f" Alt + 180 ".center(70, '┤'))
print(f" Alt + 184 ".center(70, '©'))
print(f" Alt + 185 ".center(70, '╣'))
print(f" Alt + 186 ".center(70, '║'))
print(f" Alt + 187 ".center(70, '╗'))
print(f" Alt + 188 ".center(70, '╝'))
print(f" Alt + 189 ".center(70, '¢'))
print(f" Alt + 190 ".center(70, '¥'))
print(f" Alt + 191 ".center(70, '┐'))
print(f" Alt + 192 ".center(70, '└'))
print(f" Alt + 193 ".center(70, '┴'))
print(f" Alt + 194 ".center(70, '┬'))
print(f" Alt + 195 ".center(70, '├'))
print(f" Alt + 197 ".center(70, '┼'))
print(f" Alt + 200 ".center(70, '╚'))
print(f" Alt + 201 ".center(70, '╔'))
print(f" Alt + 202 ".center(70, '╩'))
print(f" Alt + 203 ".center(70, '╦'))
print(f" Alt + 204 ".center(70, '╠'))
print(f" Alt + 205 ".center(70, '═'))
print(f" Alt + 206 ".center(70, '╬'))
print(f" Alt + 207 ".center(70, '¤'))
print(f" Alt + 208 ".center(70, 'ð'))
print(f" Alt + 209 ".center(70, 'Ð'))
print(f" Alt + 217 ".center(70, '┘'))
print(f" Alt + 218 ".center(70, '┌'))
print(f" Alt + 219 ".center(70, '█'))
print(f" Alt + 220 ".center(70, '▄'))
print(f" Alt + 221 ".center(70, '¦'))
print(f" Alt + 223 ".center(70, '▀'))
print(f" Alt + 225 ".center(70, 'ß'))
print(f" Alt + 230 ".center(70, 'µ'))
print(f" Alt + 231 ".center(70, 'þ'))
print(f" Alt + 232 ".center(70, 'Þ'))
print(f" Alt + 241 ".center(70, '±'))
print(f" Alt + 242 ".center(70, '‗'))
print(f" Alt + 245 ".center(70, '§'))
print(f" Alt + 247 ".center(70, '¸'))
print(f" Alt + 254 ".center(70, '■'))
