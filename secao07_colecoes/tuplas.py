
"""
Tuplas (tuple)

Tuplas são bastante parecidas com Listas, mas com algumas diferenças:

1 - As tuplas são representadas por parênteses (), enquanto as listas são respresentadas por olchetes [].
2 - As tuplas são imutáveis: Após criada, a tupla não muda. Toda operação em uma tupla gera uma nova tupla.


"""
#  CUIDADO 1: As tuplas são representadas por parênteses(), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

#  CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4)  # isso não é uma tupla!
print(tupla3)
print(type(tupla3))

tupla4 = (4, )  # isso é uma tupla!
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))

# CONCLUSÃO: tuplas são definidas pela vírgula e não pelo uso de parênteses.
"""
(4) -> NÃO é tupla
(4, ) -> É tupla
4, -> É tupla
"""
print('\n-----------------Tupla dinâmica com range------------------\n')

#  Tupla dinâmica com range
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

print('\n-----------------Desempacotamento de tupla-------------------\n')

#  Desempacotamento de tupla

tupla = ('Geek University', 'Programação em Python: Essencial')
#  tem que ter o mesmo número de elementos e variáveis
escola, curso = tupla

print(type(tupla))
print(escola)
print(type(escola))
print(curso)
print(type(curso))

print('\n---------------------Observações---------------------\n')

#  Métodos para adição e remoção de elementos nas tuplas não existe, pois são imutaveis;
# Soma, Valor Máximo, Valor mínimo e tamanho  somente se os valores forem todos inteiros ou reais,
tupla = (1, 2, 3, 4, 5, 6,)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

print('\n-----------------Concatenação de tuplas --------------------\n')

#  Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)  # tuplas são imutáveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2  # Tuplas são imutáveis mas podemos sobrescrever seus valores.
print(tupla1)

print('\n---------------Verificar elemento-------------------\n')

# Verificar se elemento está contido na tupla

tupla = (1, 2, 3)

print(4 in tupla)  # True or False

print('\n---------------Iterando sobre uma tupla-------------------\n')

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

print('\n---------------Contando elementos-------------------\n')

#  Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('a'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))

print('\n---------------Contando elementos-------------------\n')

#  SEMPRE Utilizar Tuplas em dados que não irão precisar de alteração.
#  Exemplo 1
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')
print(meses)

#  Acesso de elementos em uma tupla
print(meses[5])

#  Iterar com while

i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

#  Verificando índice

print(meses.index('Junho'))

#  Slicing

#  tupla[inicio:fim:passo]

print(meses[5:9])

# Por quê utilizar tuplas?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam o código mais seguro (imutáveis)

#  Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla  # Na tupla não temos o problema de Shallow Copy.

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)
