#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Trabalhando com deltas de data e hora

delta = data_final - data_inicial

"""
from rich.console import Console
import datetime

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Manipulando Data e Hora: deltas de data e hora'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on blue][bold white][center]' + texto_centralizado)

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ deltas - aniversário ↓
# --------------------------------------------------------------------------------------------------------------------

console.print("[yellow]#---------------------------------------------------------------------\n")

data_hoje = datetime.datetime.now()

# Data para ocorrer um determinado evento no futuro
proximo_aniversario = datetime.datetime.now().replace(year=2024, month=8, day=3, hour=0, minute=0, second=0)

# Calculando o delta (data_hoje - aniversario
tempo_para_evento = proximo_aniversario - data_hoje

print(type(tempo_para_evento))

# datetime.timedelta(days=365, seconds=77530, microseconds=837983)
print(repr(tempo_para_evento)) # representação do resultado (timedelta)

print(tempo_para_evento) # 365 days, 21:32:10.837983

print(tempo_para_evento.days) # 365 dias

print(tempo_para_evento.seconds) # 77530 segundos

print(tempo_para_evento.microseconds) # 837983 microsegundos

# // faz a divisão por inteiro
print(f'Faltam {tempo_para_evento.days} dias e {tempo_para_evento.seconds // 60 // 60} horas para o meu próximo '
      f'aniversário!')

console.print("[yellow]\n#---------------------------------------------------------------------\n")

# --------------------------------------------------------------------------------------------------------------------
# ↓ deltas - vencimento boleto ↓
# --------------------------------------------------------------------------------------------------------------------

data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3) # tempo para vencimento do boleto

print(f'Vencimento para: {regra_boleto}') # 3 days, 0:0:0 (regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto  # timedelta (data_da_compra + regra_boleto)

print(f'O boleto vencerá em: {vencimento_boleto}') # 2023-11-28 16:05:31.224945 (vencimento_boleto)

# Calcular a diferença entre a data de vencimento e a data atual
dias_para_vencimento = (vencimento_boleto - data_da_compra).days

print(f'Faltam {dias_para_vencimento} dias para o vencimento!')