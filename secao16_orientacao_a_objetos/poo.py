#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Programação Orientada a Objetos

- POO -> paradigma de programação que utiliza objetos
do mundo real para modelos computacionais.

- Paradigma de programação -> forma/metodologia utilizada
para pensar/desenvolver sistemas.

Principais elementos da Orientação a Objetos:
- Classe -> modelo do objeto do mundo real representado computacionalmente
- Atributo -> características do objeto
- Método -> comportamento do objeto
- Construtor -> método especial utilizado para criar objetos
- Objeto -> instância da classe

"""

import shutil
from rich.console import Console
from rich.text import Text
# from functools import wraps
# from rich import print
# from rich.padding import Padding
# from rich.style import Style
# from rich.console import Console
# from rich.table import Table
# from secao08_funcoes.minhas_funcoes import imprimir_com_cores
# from colorama import Fore

# -------------------------------------------- ↓ Bloco título ↓ --------------------------------------------

console = Console()

texto = 'Programação Orientada a Objetos'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90 + f'')
console.print(f'[on yellow][bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90 + f'')


"""# Defina a cor do texto e a altura do fundo desejadas
cor_do_texto = "blue"  # Cor do texto (ex: white, red, blue, etc.)
altura_do_fundo = 2  # Altura do fundo em número de linhas

texto = 'Programação Orientada a Objetos'  # Texto a ser exibido

tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

texto_formatado = Text()  # Crie um objeto Text para formatar o texto
texto_formatado.append(texto_centralizado, style=f" black {cor_do_texto}")

for _ in range(altura_do_fundo - 1):  # Adicione quebras de linha para controlar a altura
    largura_terminal = shutil.get_terminal_size().columns
    console.print()
    console.print("[blue]-" * int(0.5 * largura_terminal))
    console.print(texto_formatado.append(""))
    console.print("[blue]-" * int(0.5 * largura_terminal))"""

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

# console.print()
console.print("[blue]numero = 10\n")
numero = 10

console.print("[cyan]console.print(numero) => ", end='')
console.print("[blue]" + str(numero))

console.print("[cyan]console.print(type(numero)) => [/cyan]", end='')
console.print(type(numero))

# ---------------------------------------------------------------------------------------------------------------------
console.print(f'[white]-' * 90 + f'')

console.print("[blue]nome = 'Geek'\n")
nome = 'Geek'

console.print("[cyan]console.print(nome) => ", end='')
console.print("[blue]" + nome)

console.print("[cyan]console.print(type(nome)) => ", end='')
console.print(type(nome))

# ---------------------------------------------------------------------------------------------------------------------
console.print(f'[white]-' * 90 + f'')

console.print("[cyan]class Produto:\n    pass\n")


class Produto:
    pass


console.print("[blue]ps4 = Produto()\n")
ps4 = Produto()  # ps4 -> objeto da classe Produto; Produto() -> construtor da classe Produto

console.print("[cyan]console.print(ps4) => ", end='')
console.print(ps4)

console.print("[cyan]console.print(type(ps4)) => ", end='')
console.print(type(ps4))

console.print(f'[yellow]-' * 90 + f'')

# ---------------------------------------------------------------------------------------------------------------------
