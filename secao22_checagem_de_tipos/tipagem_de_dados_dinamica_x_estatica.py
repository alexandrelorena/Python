#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tipagem de dados Dinâmica x Estática

"""
from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Tipagem de dados Dinâmica x Estática'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ Tipagem de dados Dinâmica ↓
# --------------------------------------------------------------------------------------------------------------------

idade = 42  # => <class 'int'> | tipagem de dado implícita (dinâmico)

print(type(idade))

idade = 'Quarenta e dois'  # => <class 'str'> | tipagem de dado implícita (dinâmico)

print(type(idade))

# --------------------------------------------------------------------------------------------------------------------

if False:
    resultado = 1 + 'Geek'
else:
    resultado = 1 + 41

print(resultado)

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ Tipagem de dados Estática ↓
# --------------------------------------------------------------------------------------------------------------------

console.print("[yellow]----------------------------------------------------------------------\n")
