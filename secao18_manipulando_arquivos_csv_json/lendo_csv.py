#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Manipulando Arquivos CSV e Jason - Lendo arquivos CSV

CSV -> Comma Separeted Values - Valores separados por vírgula

# Separador por vírgula
    1, 2, 3, 4, 5

# Separador por ponto e vírgula
    1; 2; 3; 4; 5

# Separador por espaço

    "geek" "university" "python" "ciência" "dados"

Formas de ler dados em arquivis CSV
    - reader (listas)
    - DictReader (OrderedDicts)

"""
from rich.console import Console
# import shutil
# from rich.text import Text
# from functools import wraps
# from rich import print
# from rich.terminal_theme import TerminalTheme
# from rich.padding import Padding
# from rich.style import Style
# from rich.console import Console
# from rich.table import Table
# from secao08_funcoes.minhas_funcoes import imprimir_com_cores
# from colorama import Fore
# from passlib.hash import pbkdf2_sha256 as cryp
from csv import reader, DictReader

# -------------------------------------------- ↓ Bloco título ↓ --------------------------------------------

console = Console()

console.print()
texto = 'Manipulando Arquivos CSV e Jason'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

texto = 'Lendo arquivos CSV'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold green][center]' + texto_centralizado)
console.print(f'[white]-' * 90)

# ---------------------------------------------------------------------------------------------------------------------

texto = 'Forma incorreta >> Possível de se trabalhar mas não é o ideal (trabalhoso).'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
# console.print(f'[yellow]-' * 90)
console.print(f'[bold red][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("[white]\nnome_arquivo = 'lutadores.csv'\n\n[green]try:\n"
              ""
              "    [green]with [black]open(nome_arquivo, 'r', encoding='utf-8') as arquivo:\n"
              ""
              "        []dados = arquivo.read()\n\n"
              "[green]except [black]UnicodeDecodeError as e:\n"
              ""
              "    print(f'Erro de decodificação Unicode: {e}')\n")


nome_arquivo = 'lutadores.csv'

console.print(f'[cyan]dados = dados.split(",")[2:]  # separando e usando slice')

console.print()

try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = arquivo.read()

except UnicodeDecodeError as e:
    print(f"Erro de decodificação Unicode: {e}")


nome_arquivo = 'lutadores.csv'

try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = arquivo.read()
        # Faça algo com os dados aqui

except UnicodeDecodeError as e:
    print(f"Erro de decodificação Unicode: {e}")

dados = dados.split(',')[2:]  # separando e usando slice

console.print("# ----------------------------------------------------------------------------------------")

console.print(f'[blue]{dados}')

console.print("# ----------------------------------------------------------------------------------------")

console.print()

console.print("print(type(leitor_csv))")

console.print()

console.print(f'[cyan]tipo de dados:[/cyan] {type(dados)}')

console.print()

# ---------------------------------------------------------------------------------------------------------------------

texto = 'Formas corretas - 1. Usando reader (retorna um interator)'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold red][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("[white]\nnome_arquivo = 'lutadores.csv'\n\n[green]try:\n"
              ""
              "    [green]with [black]open(nome_arquivo, 'r', encoding='utf-8') as arquivo:\n"
              ""
              "        leitor_csv = reader(arquivo)\n"
              "        next(leitor_csv)  [white]# Pular o cabeçalho\n\n"
              "[green]        for linha in leitor_csv:\n            [white]# Cada linha é uma lista\n"
              ""
              "            [black]console.print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros')"
              "\n\n[green]except [black]UnicodeDecodeError as e:\n"
              "    print(f'Erro de decodificação Unicode: {e}')\n")

console.print("# ----------------------------------------------------------------------------------------")

try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        leitor_csv = reader(arquivo)
        next(leitor_csv)  # Pular o cabeçalho

        for linha in leitor_csv:
            # Cada linha é uma lista
            console.print(f'[blue]{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros')

except UnicodeDecodeError as e:
    print(f"Erro de decodificação Unicode: {e}")

console.print("# ----------------------------------------------------------------------------------------")

console.print()

console.print("print(type(leitor_csv))")

console.print()

console.print(f'[cyan]tipo de dados:[/cyan] {type(leitor_csv)}')

console.print()

# ---------------------------------------------------------------------------------------------------------------------

texto = 'Formas corretas - 2. Usando DictReader (retorna um interator)'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold red][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print()

console.print("[green]try:\n"
              ""
              "    [green]with [black]open(nome_arquivo, 'r', encoding='utf-8') as arquivo:\n"
              ""
              "        leitor_csv = DictReader(arquivo)\n"
              "        [white]# leitor_csv = DictReader(arquivo, delimiter=',')\n"
              "        [white]# Se o delimitador não for a vírgula, e sim o ponto e vírgula (;), então você precisará "
              "incluir delimiter=';'\n"
              ""
              "        [green]for [black]linha in leitor_csv:\n"
              "[white]            # Cada linha é um OrderedDict\n"
              ""
              "            [black]console.print(f'{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura"
              " (em cm)']}')"
              "\n\n[green]except [black]UnicodeDecodeError as e:\n"
              "    print(f'Erro de decodificação Unicode: {e}')\n")

console.print("# ----------------------------------------------------------------------------------------")

try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        leitor_csv = DictReader(arquivo)
        # leitor_csv = DictReader(arquivo, delimiter=',')
        # Se o delimitador não for a vírgula, e sim o ponto e vírgula (;), então você precisará incluir delimiter=';'
        for linha in leitor_csv:
            # Cada linha é um OrderedDict
            console.print(f"[blue]{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")

except UnicodeDecodeError as e:
    print(f"Erro de decodificação Unicode: {e}")

console.print("# ----------------------------------------------------------------------------------------")

console.print()

console.print("print(type(leitor_csv))")

console.print()

console.print(f'[cyan]tipo de dados:[/cyan] {type(leitor_csv)}')

console.print()