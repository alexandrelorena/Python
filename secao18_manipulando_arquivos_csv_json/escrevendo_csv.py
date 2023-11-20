#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Escrevendo em Arquivos CSV

reader() > (leitor)

writer() > (escritor) - Gera um objeto para que possamos escrever em um arquivo .CSV

writerow() -> Utilizamos para escrever cada linha. Este método recebe uma lista.


"""
import os

from rich.console import Console

from csv import DictWriter, DictReader

# -------------------------------------------- ↓ Bloco título ↓ --------------------------------------------

console = Console()

console.print()
texto = 'Manipulando Arquivos CSV e Jason'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

texto = 'Escrevendo em Arquivos CSV'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
# console.print(f'[bold green][center]' + texto_centralizado)
# console.print(f'[white]-' * 90)

# ---------------------------------------------------------------------------------------------------------------------

texto = 'Escrevendo em Arquivos CSV - Utilizando writer (Listas)'
tamanho_desejado = 90  # Largura do bloco
# noinspection PyRedeclaration
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
# console.print(f'[yellow]-' * 90)
console.print(f'[bold blue][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("[black]with open('filmes.csv', 'w', encoding='utf-8') as arquivo:\n"
              "    escritor_csv = writer(arquivo)\n    filme = None\n    escritor_csv.writerow"
              "(['Título', 'Gênero', 'Duração'])  [qhite]# este método trabalha com lista\n"
              "[black]    while filme != 'sair':\n        filme = input('Informe o nome do filme: ')\n"
              "        if filme != 'sair':\n            genero = input('Informe o gênero do filme: ')\n"
              "            duracao = input('Informe a duração do filme: ')\n"
              "            escritor_csv.writerow([filme, genero, duracao])\n\n")

# with open('filmes.csv', 'w', encoding='utf-8') as arquivo:
#     escritor_csv = writer(arquivo)
#     filme = None
#     escritor_csv.writerow(['Título', 'Gênero', 'Duração'])  # este método trabalha com lista
#     while filme != 'sair':
#         filme = input('Informe o nome do filme: ')
#         if filme != 'sair':
#             genero = input('Informe o gênero do filme: ')
#             duracao = input('Informe a duração do filme: ')
#             escritor_csv.writerow([filme, genero, duracao])
# ---------------------------------------------------------------------------------------------------------------------

texto = 'Escrevendo em Arquivos CSV - Utilizando DictWriter (Dicionário)'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold blue][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)

console.print("[white]OBS: As chaves dos dicionários DEVEM ser as mesmas utilizadas como cabeçalho[/white]\n\n"
              "arquivo_csv = 'filmes.csv'\ncabecalho = ['Título', 'Gênero', 'Duração']\n\n"
              "[white] Verifica se o arquivo já existe[/white]\narquivo_existe = os.path.isfile(arquivo_csv)\n\n"
              "[white]Verifica se o arquivo existente possui cabeçalho[/white]\narquivo_com_cabecalho = False\n"
              "[black]if arquivo_existe:\n    with open(arquivo_csv, 'r', encoding='utf-8') as arquivo_leitura:\n"
              "        leitor_csv = DictReader(arquivo_leitura)\n        if cabecalho == leitor_csv.fieldnames:\n"
              "            arquivo_com_cabecalho = True\n\n"
              "[white]Abre o arquivo no modo leitura ou cria se não existir[/white]\n"
              "with open(arquivo_csv, 'a', encoding='utf-8', newline='') as arquivo:\n    escritor_csv = DictWriter"
              "(arquivo, fieldnames=cabecalho)\n\n"
              "    [white]Se o arquivo não existir ou não possuir cabeçalho, escreve o cabeçalho[/white]\n"
              "    if not arquivo_existe or not arquivo_com_cabecalho:\n        escritor_csv.writeheader()\n"
              "        arquivo.write(---------------------\\n)\n\n"
              "    filme = None\n    while filme != 'sair':\n        filme = input('Informe o nome do filme "
              "(ou 'sair' para encerrar): ')\n        if filme != 'sair':\n            genero = input('Informe o gênero"
              " do filme: ')\n            duracao = input('Informe a duração do filme: ')\n\n"
              "            [white] Escreve o filme no CSV[/white]\n            "
              "escritor_csv.writerow({'Título': filme, 'Gênero': genero, 'Duração': duracao})\n\n")

# OBS: As chaves dos dicionários DEVEM ser as mesmas utilizadas como cabeçalho

arquivo_csv = 'filmes.csv'
cabecalho = ['Título', 'Gênero', 'Duração']

# Verifica se o arquivo já existe
arquivo_existe = os.path.isfile(arquivo_csv)

# Verifica se o arquivo existente possui cabeçalho
arquivo_com_cabecalho = False
if arquivo_existe:
    with open(arquivo_csv, 'r', encoding='utf-8') as arquivo_leitura:
        leitor_csv = DictReader(arquivo_leitura)
        if cabecalho == leitor_csv.fieldnames:
            arquivo_com_cabecalho = True

# Abre o arquivo no modo leitura ou cria se não existir
with open(arquivo_csv, 'a', encoding='utf-8', newline='') as arquivo:
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)

    # Se o arquivo não existir ou não possuir cabeçalho, escreve o cabeçalho
    if not arquivo_existe or not arquivo_com_cabecalho:
        escritor_csv.writeheader()
        arquivo.write("---------------------\n")

    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme (ou "sair" para encerrar): ')
        if filme != 'sair':
            genero = input('Informe o gênero do filme: ')
            duracao = input('Informe a duração do filme: ')

            # Adiciona uma linha em branco antes de cada filme, exceto antes do primeiro
            # if filme.lower() != 'sair':
            #     arquivo.write("\n")

            # Escreve o filme no CSV
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})

console.print("# ----------------------------------------------------------------------------------------")
