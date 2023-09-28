
"""
Módulo Collections - Ordered Dict

Collections >> High-performance Container Datetypes

obs: Dicionário que garante a ordem de inserção dos elementos
"""

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(dicionario)
print('\n-------------------------------------------------------------\n')
for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

from collections import OrderedDict

print('\n-------------------------------------------------------------\n')
dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

print('\n-----------------No dicionario não importa a ordem----------------------\n')

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)
# True
print('\n----------No OrderedDict a ordem dos elementos importa-----------\n')
#  Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # pra ser igual a ordem tem que ser igual
# False
