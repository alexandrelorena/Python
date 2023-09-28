
"""
Mapas -> conhecidos em Python como Dicionários
- são representados por chaves {}

"""
receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

#  Iterar sobre dicionários

for chave in receita:  # imprimindo chave
    print(chave)

for chave in receita:  # imprimindo valor
    print(receita[chave])
print('\n-----------------imprimindo chave e valor-------------------\n')
for chave in receita:
    print(f'Em {chave} recebi R$ '
          f'{receita[chave]}')
print('\n------------------Dicionário de chaves----------------------\n')

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

print('\n--------------Dicionário de valores-------------------\n')

print(receita.values())

for valor in receita.values():
    print(valor)

print('\n--------------Desempacotamento de Dicionários-------------------\n')

print(receita.items())  # exibe uma lista contendo tuplas chave-valor

for chave, valor in receita.items():
    print(f'chave -> {chave} | valor -> {valor}')

print('\n-----------Soma, Valor Máximo, Valor mínimo e tamanho--------------\n')

# Soma, Valor Máximo, Valor mínimo e tamanho  somente se os valores forem todos inteiros ou reais,

print('Soma:', sum(receita.values()))
print('Valor máximo:', max(receita.values()))
print('Valor mínimo:', min(receita.values()))
print('Qtde de elementos:', len(receita.values()))
