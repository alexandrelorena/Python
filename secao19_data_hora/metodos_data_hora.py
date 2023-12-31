#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Métodos de Data e Hora
"""

import functools
from googletrans import Translator
from rich.console import Console
import datetime
import timeit
# from textblob import TextBlob

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Métodos de Data e Hora'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on blue][bold white][center]' + texto_centralizado)

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ Método: datetime.now() | datetime.today() ↓
# --------------------------------------------------------------------------------------------------------------------

console.print("[green]#---------------------------------------------------------------------\n")

data_hoje = datetime.datetime.now()

agora = datetime.datetime.now()  # pode especificar um timezone (Fuso Horário

print(f'agora: {agora}')  # 2023-11-28 16:05:31.224945 (agora)

print(type(agora))

print(repr(agora))

hoje = datetime.datetime.today()

print()

print(f'hoje: {hoje}')  # 2023-11-28 (hoje)

print(type(hoje))

print(repr(hoje))

print()

console.print("[green]#---------------------------------------------------------------------\n")

# --------------------------------------------------------------------------------------------------------------------
# ↓ Método combine() | Mudanças ocorrendo à meia-noite ↓
# --------------------------------------------------------------------------------------------------------------------

# combine() - > combina os valores passados

# datetime.time() -> passa horas, minutos e segundos como zero

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)

print(type(manutencao))

print(repr(manutencao))

console.print("[green]#---------------------------------------------------------------------\n")

# --------------------------------------------------------------------------------------------------------------------
# ↓ Método weekday() | Encontrar o dia da semana ↓
# --------------------------------------------------------------------------------------------------------------------

# Os dias da semana do método weekday() iniciam em zero (segunda-feira)

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

# 0 - Segunda-feira (Monday)
# 1 - Terça-feira (Tuesday)
# 2 - Quarta-feira (Wednesday)
# 3 - Quinta-feira (Thursday)
# 4 - Sexa-feira (Friday)
# 5 - Sábado (Saturday)
# 6 - Domingo (Sunday)

dias_da_semana = ['na Segunda-feira', 'na Terça-feira', 'na Quarta-feira', 'na Quinta-feira', 'na Sexta-feira',
                  'no Sábado', 'no Domingo']

print(f'A manutenção será feita {dias_da_semana[manutencao.weekday()]}!')

aniversario = input('Qual sua data de nascimento? dd/mm/yyyy: ')

aniversario = aniversario.split('/')

aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Você nasceu em uma segunda-feira')
elif aniversario.weekday() == 1:
    print('Você nasceu em uma terça-feira')
elif aniversario.weekday() == 2:
    print('Você nasceu em uma quarta-feira')
elif aniversario.weekday() == 3:
    print('Você nasceu em uma quinta-feira')
elif aniversario.weekday() == 4:
    print('Você nasceu em uma sexta-feira')
elif aniversario.weekday() == 5:
    print('Você nasceu em um sábado')
elif aniversario.weekday() == 6:
    print('Você nasceu em um domingo')

# --------------------------------------------------------------------------------------------------------------------
# ↓ Método strftime() | formatando datas/horas ↓
# --------------------------------------------------------------------------------------------------------------------

# dd/mm/yyy hh:mm - formato brasileiro

hoje = datetime.datetime.today()

print(hoje)  # formato em inglês

hoje_formatado = hoje.strftime('%d/%b/%Y %H:%M')

#  /%Y: 'b' minúsculo - nome do mês abreviado (em inglês)
#  /%Y: 'B' maiúsculo - nome do mês (em inglês)

#  /%y: 'y' minúsculo - ano com dois digitos
#  /%Y: 'Y' maiúsculo - ano com quatro digitos

print(hoje_formatado)  # formato em português


def formata_data(data):
    if data.month == 1:
        return f'{data.day} de janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de dezembro de {data.year}'


hoje = datetime.datetime.today()

print((formata_data(hoje)))

# --------------------------------------------------------------------------------------------------------------------
# ↓ Formatando datas - strftime (converte datetime para string) - usando Translator (googletrans) ↓
# --------------------------------------------------------------------------------------------------------------------

# def formata_data(data):
#     return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"


def formata_data(data):
    translator = Translator()
    month_translation = translator.translate(data.strftime('%B'), dest='pt').text
    return f"{data.day} de {month_translation} de {data.year}"


hoje = datetime.datetime.today()

print((formata_data(hoje)))

# --------------------------------------------------------------------------------------------------------------------
# ↓ Formatando datas - strptime -> converte string para datetime ↓
# --------------------------------------------------------------------------------------------------------------------

nascimento = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')

print(nascimento)

nascimento = input('Qual sua data de nascimento? (dd/mm/yyyy): ')

nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')

print(nascimento)

# --------------------------------------------------------------------------------------------------------------------
# ↓ Formatando datas - datetime.time ↓
# --------------------------------------------------------------------------------------------------------------------

almoco = datetime.time(12, 30, 0)  # Recebe 3 parâmetros:hora, minuto, segundo

print(f'O Almoço é as {almoco} horas')

# --------------------------------------------------------------------------------------------------------------------
# ↓ Formatando datas — marcando tempo de execução com timeit ↓
# --------------------------------------------------------------------------------------------------------------------


# é um 'generator' — recebe 2 parâmetros: uma 'string' e o número de vezes

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f'Loop for: {tempo}')

# List Comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(f'List Comprehension: {tempo}')

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(f'Map: {tempo}')

# --------------------------------------------------------------------------------------------------------------------
# ↓ Formatando datas — marcando tempo de execução com functools ↓
# --------------------------------------------------------------------------------------------------------------------


def teste(n):
    soma = 0
    for num in range(n * 100):
        soma = soma + num ** num + 4
    return soma


print(f'Tempo executado sem functools: {timeit.timeit(lambda: teste(2), number=1000)}')  # timeit.timeit espera uma
# função sem
# argumentos, por isso usamos o lambda ao passar o resultado de uma função.
"""
A função timeit.timeit executa a declaração fornecida um milhão de vezes por padrão. No entanto, você pode controlar o 
número de execuções definindo o argumento number: number=1000

O argumento number é um parâmetro opcional. Por padrão, o valor do argumento number é 1000. 
Se você deseja executar o programa por mais de um milhão de vezes, defina o valor do argumento number como um número 
maior.

"""

print()

print(f'Tempo executado com functools: {timeit.timeit(functools.partial(teste, 2), number=1000)}')
