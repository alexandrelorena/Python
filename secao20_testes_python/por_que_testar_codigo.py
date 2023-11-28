#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Por que testar nosso código?

Testes automatizados!

            Aplicação web
-----------------------------------
/                                 /
/      frontend e backend         /
-----------------------------------
/                                 /
/      testes automatizados       /
-----------------------------------

Por que testar nosso código?
    — reduzir bugs;
    — manter a qualidade do código;
    — manter a qualidade do software;
    — testes garantem que bugs que foram corrigidos anteriormente continuem sendo corrigidos;
    — testes garantem que a refatoração não tragam novos bugs;
    — testes garantem que o código e o software funcionem corretamente;

TDD — Test Driven Development (Desenvolvimento Guiado por Testes)

Com TDD são utiizados estágios de desenvolvimento, como:

    — Você escreve o seu teste primeiro;
    — Você escreve o código mínimo suficiente para fazer o teste passar (executar com sucesso).
    — Refatoração do que foi implementado;
    — Testa novamente;

RGR — Red Green Refactor (Refatoração de Código)
1 — RED
2 — GREEN
3 — REFACTOR

Com RGR você pode refatorar o código e testar novamente.

"""

# import functools
# from googletrans import Translator
from rich.console import Console
# import datetime
# from textblob import TextBlob

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Métodos de Data e Hora'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ Método: datetime.now() | datetime.today() ↓
# --------------------------------------------------------------------------------------------------------------------

console.print("[yellow]#---------------------------------------------------------------------\n")


