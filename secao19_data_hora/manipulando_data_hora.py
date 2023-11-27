#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Manipulando Data e Hora : datetime
"""

from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Manipulando Data e Hora : datetime'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on blue][bold white][center]' + texto_centralizado)

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ datetime ↓
# --------------------------------------------------------------------------------------------------------------------

console.print("[yellow]#---------------------------------------------------------------------\n")

import datetime

#  print(dir(datetime))

print(f'MAXYEAR: {datetime.MAXYEAR}')  # 9999 -> Ano máximo permitido pelo Python (datetime.MAXYEAR)

print(f'MINYEAR: {datetime.MINYEAR}')  # 1 -> Ano mínimo permitido pelo Python (datetime.MINYEAR)

console.print("[yellow]\n#---------------------------------------------------------------------\n")

#  Retorna a date e hora corrente -> formato em inglês
print(f'datetime.now(): {datetime.datetime.now()}')  # -> 2023-11-25 16:05:31.224945 (datetime.datetime.now())

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(f'representação: {(repr(datetime.datetime.now()))}') # -> datetime.datetime(2023, 25, 16, 8, 31, 394238)

console.print("[yellow]\n#---------------------------------------------------------------------\n")

# --------------------------------------------------------------------------------------------------------------------
#  ↓ replace ↓ -> método usado para fazer ajustes no formato
# --------------------------------------------------------------------------------------------------------------------

inicio = datetime.datetime.now()

print(f'início -> datetime.now(): {inicio}')  # -> 2023-11-25 16:05:31.224945 (inicio)

#  Alterar o horário para 16h, 0 minutos, 0 segundos, 0 microsegundos
inicio = inicio.replace(year=2030, month=11, day=25, hour=16, minute=14, second=0, microsecond=0)

print(f'replace: {inicio}')  # -> 2023-11-25 16:14:00.000000 (inicio)

console.print("[yellow]\n#---------------------------------------------------------------------\n")

# --------------------------------------------------------------------------------------------------------------------
#  ↓ tratando dados recebidos pelo usuário ↓ -> fazendo split e convertendo para int
# --------------------------------------------------------------------------------------------------------------------

evento = datetime.datetime(2040, 11, 25, 16, 14, 0, 0)

print(f'evento: {evento}')

print(type(evento))

print(type('31/12/2023'))

print(evento)

nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ')

print(nascimento)

nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))  # opção 1
# nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y') # convertendo a string to datetime  opção 2

print(nascimento)  # mostra os dados no formato datetime (inglês)

print(type(nascimento))

# --------------------------------------------------------------------------------------------------------------------
#  ↓ Acesso individual dos elementos de data e hora ↓
# --------------------------------------------------------------------------------------------------------------------

print(evento.year)  # Ano

print(evento.month)  # Mês

print(evento.day)  # Dia

print(evento.hour) # Hora

print(evento.minute) # Minuto

print(evento.second) # Segundo

print(evento.microsecond) # Microsegundo

print(dir(evento))  # mostra atributos possíveis para o objeto