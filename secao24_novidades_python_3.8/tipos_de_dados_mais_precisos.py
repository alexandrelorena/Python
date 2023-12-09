#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tipos_de_dados_mais_precisos

• Literal Type
• Union Type
• Final
• Typed-Dictionary
• Protocols

"""
from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Tipos de dados mais precisos'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

console.print("[yellow]----------------------------------------------------------------------")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ Tipos de dados mais precisos ↓
# --------------------------------------------------------------------------------------------------------------------

def dobro(valor: int) -> int:
    return valor * 2

print(dobro(8))
print(dobro(42))

console.print("[yellow]----------------------------------------------------------------------")

texto = 'Literal Type calcula_v1'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)

from typing import Literal

# def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
#     pass


def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    elif operacao == '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    elif operacao == '/':
        print(f'{num1} / {num2} = {num1 / num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}!')  # !r coloca o erro entre aspas simples ''

calcula_v1('+', 6, 4)
calcula_v1('-', 6, 4)
calcula_v1('*', 6, 4)
calcula_v1('/', 6, 4)
# calcula_v1('**', 6, 4)  # raise ValueError(f'Operação inválida {operacao!r}!') ValueError: Operação inválida '**'!

console.print("[yellow]----------------------------------------------------------------------")

texto = 'Literal Type calcula_v2'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)
def calcula_v2(operacao: Literal['+', '-', '*', '/'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    elif operacao == '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    elif operacao == '/':
        print(f'{num1} / {num2} = {num1 / num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}!')  # !r coloca o erro entre aspas simples ''

calcula_v2('+', 3, 2)
calcula_v2('-', 4, 5)
calcula_v2('*', 2, 8)
calcula_v2('/', 5, 2)
# calcula_v2('**', 6, 4)  # raise ValueError(f'Operação inválida {operacao!r}!') ValueError: Operação inválida '**'!

console.print("[yellow]----------------------------------------------------------------------")

texto = 'Union'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[on yellow][bold white][center]' + texto_centralizado)

from typing import Union
def soma(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1 + num2

    if resultado > 50:
        return f'O valor {resultado} é muito grande!'
    else:
        return resultado

print(soma(4, 8))
print(soma(40, 11))
print(soma(2, 5))
soma(40, 11)
soma(2, 5)

console.print("[yellow]----------------------------------------------------------------------")

texto = 'Final'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[on yellow][bold white][center]' + texto_centralizado)

from typing import Final

NOME: Final = 'Geek'

print(NOME)

# NOME = 'University'

print(NOME)

from typing import final

@final
class Pessoa:
    pass

class Estudante:
    pass

    @final
    def estudar(self):
        print('Estou estudando...')

class Estagiario(Estudante):
    pass

    # def estudar(self):
    #     print('Estudando e estagiando...')

console.print("[yellow]----------------------------------------------------------------------")

texto = 'Typed Dictionaries'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[on yellow][bold white][center]' + texto_centralizado)

from typing import TypedDict

class CursoPython(TypedDict):  # dicionártio tipado
    versao: str
    atualizado: int

geek = CursoPython(versao='3.8.5', atualizado=2020)


print(geek)

console.print("[yellow]----------------------------------------------------------------------")

texto = 'Protocols'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[on yellow][bold white][center]' + texto_centralizado)

from typing import Protocol

class Curso(Protocol):
    titulo: str

def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')

class Venda:
    titulo = 'Oi'

v1 = Venda()
# c1 = Curso()
# c1.titulo = 'Programação em Python'

# estudar(c1)
estudar(v1)
