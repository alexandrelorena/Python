
"""
Conjuntos

- conjuntos são chamados de Sets.
- Sets (conjuntos) não pssuem valores duplicados
- Sets (conjuntos) não pssuem valores ordenados
- Elementos não sao indexados (acessados via índice)

Utilizar para armazenar elementos sem se importar com a ordenação, chaves, valores e itens duplicados.

São referenciados em Python  com chaves {}

Diferenças  entre Conjuntos (Sets) e Mapas (Dicionários) em Python:
    - Um dicion[ario tem chave/valor;
    - Um conjunto tem apenas valor;

"""
print('\n-------------Definindo um conjunto-Forma 1------------\n')

s = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}  # temos valores repetidos

# Forma 1

print(s)  # não imprime valores repetidos
print(type(s))

# O conjunto ignora itens duplicados sem gerar erro.

print('\n---------------Forma 2 - mais comum-----------------\n')
# Forma 2 - mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

print('\n----------------set de string-------------------\n')

#  set de string
s = set('Gek Univerzity')
print('Set de String: ', s)
print(type(s))

print('\n----------------set de lista-------------------\n')

#  set de lista
lista = [1, 2, 3, 4, 5, 6, 7, 4, 3, 2]  # O conjunto ignora itens duplicados
print('Set de Lista: ', set(lista))
print(type(lista))

print('\n----------------set de tupla-------------------\n')

#  set de tupla
tupla = (1, 2, 3, 4, 5, 6, 7)  # O conjunto ignora itens duplicados
print('Set de Tupla: ', set(tupla))
print(type(tupla))

print('\n----------Não há ordem ou duplicados em Conjuntos-----------\n')

# Não há ordem ou duplicados em Conjuntos

lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} >> com {len(lista)} elementos')

tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla} >> com {len(tupla)} elementos')

dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionario: {dicionario} >> com {len(dicionario)} elementos')  # não aceitam chaves duplicadas

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} >> com {len(conjunto)} elementos')  # não aceitam valores duplicados

print('\n----------Em SETS podemos misturar dados-----------\n')

#  Em SETS podemos misturar dados como em todo conjunto Python

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

print('\n----------iterando Set-----------\n')
#  iterando Set

for valor in s:
    print(valor)

print('\n----------usos interessantes com Set-----------\n')

#  lista
cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']
print(cidades)
print(len(cidades))
print(type(cidades))

print(len(set(cidades)))  # printando o número da lista sem itens repeditos

print('\n----------adicionando elementos em um conjunto-----------\n')

s = {1, 2, 3}
print(s)

s.add(4)
s.add(4)
print(s)  # conjuntos não são imutáveis como as tuplas

#  duplicidade não gera erro, apenas é ignorado

print('\n----------removendo elementos em um conjunto-----------\n')

s = {1, 2, 3}
print(s)

#  Forma 1
s.remove(3)  # informamos o valor a ser removido - NÃO é índice. Conjuntos não tem índices;
print(s)

#  Forma 2
s.discard(2)  # não é gerado erro se o valor não for encontrado
print(s)

print('\n----------copiando um conjunto para outro-----------\n')
s = {1, 2, 3}

#  Forma 1 - Deep Copy
novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

#  Forma 2 - Shallow Copy

novo = s

novo.add(4)

print(novo)
print(s)

print('\n----------removendo um item de um conjunto -----------\n')

s = {1, 2, 3}
print(s)
print(type(s))
s.clear()
print(s)

print('\n----------Métodos matemáticos de Conjuntos 1-----------\n')

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

#  Forma 1 - Union

unicos1 = estudantes_python.union(estudantes_java)
#  {'Julia', 'Ana', 'Guilherme', 'Fernando', 'Pedro', 'Marcos', 'Gustavo', 'Ellen', 'Pa

# unicos1 = estudantes_java.union(estudantes_python)
# {'Ana', 'Julia', 'Pedro', 'Marcos', 'Guilherme', 'Fernando', 'Ellen', 'Patricia', 'Gustavo'}

print('Únicos com union >>', unicos1)

#  Forma 2 - Pipe |

unicos2 = estudantes_python | estudantes_java
print('Únicos com | (pipe) >>', unicos2)

print('\n----------Métodos matemáticos de Conjuntos 2----------\n')

# Forma 1 - Intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print('Ambos com intersection >>', ambos1)

ambos2 = estudantes_java.intersection(estudantes_python)
print(ambos2)

#  Forma 2 - & (e comercial)

ambos2 = estudantes_python & estudantes_java
print('Ambos com & >>', ambos2)

print('\n----------Métodos matemáticos de Conjuntos 3----------\n')

#  Forma 1 - difference

so_python = estudantes_python.difference(estudantes_java)
print('Só python >>', so_python)

so_java = estudantes_java.difference(estudantes_python)
print('Só java >>', so_java)

print('\n--------------- Soma, valor máximo, valor mínimo, tamanho ----------------\n')

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
