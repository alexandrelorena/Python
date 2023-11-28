#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assertions (Afirmações/Checagens/Questionamentos)

- Permite realizar simples afirmações utilizadas nos testes
- Validar se uma expressão é válida ou não:
    se verdadeiro, retorna None;
    se falso, levanta um erro do tipo AssertionError.

OBS: Não é possível gerar uma mensagem de erro personalizada
OBS: A palavra 'assert' pode ser utilizada em qualquer função ou código (não exclusivamente nos teste)


"""


# import functools
# from googletrans import Translator
from rich.console import Console
# import datetime
# from textblob import TextBlob

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Assertions (Afirmações/Checagens/Questionamentos)'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ Método: datetime.now() | datetime.today() ↓
# --------------------------------------------------------------------------------------------------------------------



console.print("[yellow]#---------------------------------------------------------------------\n")
