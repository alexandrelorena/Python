#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assertions (Afirmações/Checagens/Questionamentos)

- Permite realizar simples afirmações utilizadas nos testes
— Validar se uma expressão é válida ou não:
    se verdadeiro, retorna None;
    se falso, levanta um erro do tipo AssertionError.

OBS: Não é possível gerar uma mensagem de erro personalizada
OBS: A palavra 'assert' pode ser utilizada em qualquer função ou código (não exclusivamente nos teste)

#  ALERTA!!!  Cuidado ao utilizar 'assert'.
     - parâmetro -O => nenhum assertion será validado.

"""

from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Assertions (Afirmações/Checagens/Questionamentos)'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ assert ↓
# --------------------------------------------------------------------------------------------------------------------


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, "Os valores devem ser positivos"
    return a + b



ret = soma_numeros_positivos(2, 4)  # 6
# ret = soma_numeros_positivos(-2, 4)  # AssertionError
print(ret)



def comer_fast_food(comida,):
    assert comida in ["pizza", "hamburguer", "sushi"], "Comida inválida"
    return f"Comendo {comida}"



comida = input("Qual a sua comida favorita? ")
print(comer_fast_food(comida))

console.print("[yellow]#---------------------------------------------------------------------\n")

