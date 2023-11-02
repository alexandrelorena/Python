#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
minhas_funcoes
"""
from termcolor import colored


def imprimir_com_cores(iteravel):
    cores = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    cor_index = 0

    nome_atual = ''

    for letra in iteravel:
        if letra != ' ':
            cor = cores[cor_index % len(cores)]
            letra_colorida = colored(letra, cor)
            nome_atual += letra_colorida
            cor_index += 2
        else:
            print(nome_atual, end=' ')
            nome_atual = ''

    print(nome_atual)  # Imprimir o último nome
