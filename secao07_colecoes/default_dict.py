"""
Módulo Collections - Default Dict

Collections >> High-performance Container Datetypes

Default Dict ->

obs: Lambdas são funções sem nome. Podem ou não receber parâmetros de entrada
e retornar valores.
"""
from collections import defaultdict

dicionario = {'curso': 'Programação em Python'}

print(dicionario)
print('\n-----------------------\n')
print(dicionario['curso'])
print('\n-----------------------\n')
# print(dicionario['outro']) # ??? Key Error

#  Fazendo import


dicionario = defaultdict(lambda: 0)

print(dicionario)
print('\n-----------------------\n')
# dicionario['curso'] = 'Programação em Python'
print('\n-----------------------\n')
print(dicionario)
print('\n-----------------------\n')
print(dicionario['outro'])  # KeyError no dicionario comum, mas aqui não
# defaultdict(<function <lambda> at 0x0000016815AA4C10>, {'curso': 'Programação em Python', 'outro': 0})  >> o 'zero'
# é o valor de defaultdict adicionado ao lambda.
print('\n-----------------------\n')
print(dicionario)
