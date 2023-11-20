#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Conhecendo o Pickle

Sua função é realizar o seguinte processo:

    Objeto Python -> Binarização

    Binarização -> Objeto Python

Este processo é chamado de serialização/deserialização

OBS: O módulo Pickle não é seguro contra dados maliciosos. (não recomendado utilizar de fontes desconhecidas)


"""

from rich.console import Console
import pickle

# -------------------------------------------- ↓ Bloco título ↓ --------------------------------------------

console = Console()

console.print()
texto = 'Conhecendo o Pickle'
tamanho_desejado = 80  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

texto = 'Fazendo a escrita - arquivo serializado'
tamanho_desejado = 80  # Largura do bloco
# noinspection PyRedeclaration
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 80)
console.print(f'[bold blue][center]' + texto_centralizado)
console.print(f'[yellow]-' * 80)

# ---------------------------------------------------------------------------------------------------------------------

console.print()

console.print("[green]class [black]Animal:\n    [green]def[black] __init__(self, nome):\n        self.__nome = nome\n\n"
              "    [green]def [black]comer(self):\n        print(f'{self.__nome} está comendo...')\n\n"
              "[green]class [black]Gato(Animal):\n    [green]def [black]__init__(self, nome):\n        "
              "super(). __init__(nome)\n\n"
              "    [green]def [black]mia(self):\n        console.print(f'{self._Animal__nome} está miando...')\n\n"
              "[green]class [black]Cachorro(Animal):\n    [green]def [black]__init__(self, nome):\n        "
              "super(). __init__(nome)\n\n"
              "    [green]def [black]late(self):\n        console.print(f'{self._Animal__nome} está latindo...\n\n"
              ""
              "felix = Gato('Felix')\n\npluto = Cachorro('Pluto')\n\n"
              ""
              "[green]with [black]open('animais.pickle', 'wb') [green]as [black]arquivo:  [cyan]# wb -> w = write; b = "
              "binario[/cyan]"
              "\n"
              "    pickle.dump((felix, pluto), arquivo)  [cyan]# recebe 2 parametros: nome e arquivo onde será feita a "
              "escrita[/cyan]")


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Gato(Animal):
    def __init__(self, nome):
        super(). __init__(nome)

    def mia(self):
        console.print(f'{self.nome} está miando...')


class Cachorro(Animal):
    def __init__(self, nome):
        super(). __init__(nome)

    def late(self):
        console.print(f'{self.nome} está latindo...')


felix = Gato('Felix')

pluto = Cachorro('Pluto')

with open('animais.pickle', 'wb') as arquivo:  # wb -> w = write; b = binario
    pickle.dump((felix, pluto), arquivo)  # recebe 2 parametros: nome e arquivo onde será feita a escrita

console.print()

# ---------------------------------------------------------------------------------------------------------------------

texto = 'Fazendo a leitura de dados em arquivos pickle'
tamanho_desejado = 80  # Largura do bloco
# noinspection PyRedeclaration
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 80)
console.print(f'[bold blue][center]' + texto_centralizado)
console.print(f'[yellow]-' * 80)

# ---------------------------------------------------------------------------------------------------------------------

console.print()

console.print("[green]with [black]open('animais.pickle', 'rb') [green]as [black]arquivo:\n    gato, cachorro = pickle."
              "load(arquivo)\n"
              "    console.print(f'O gato chama-se {gato.nome}')\n    gato.mia()\n    console.print(f'O tipo do gato é"
              " {type(gato)}')\n\n"
              "    console.print(f'O cachorro chama-se {cachorro.nome}')\n    cachorro.late()\n"
              "    console.print(f'O tipo do cachorro é {type(cachorro)}')\n")

with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    console.print(f'O gato chama-se {gato.nome}')
    gato.mia()
    console.print(f'O tipo do gato é {type(gato)}')

    console.print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()
    console.print(f'O tipo do cachorro é {type(cachorro)}')

console.print()
